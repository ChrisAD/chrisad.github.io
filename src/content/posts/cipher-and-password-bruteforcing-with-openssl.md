---
title: "Cipher and password bruteforcing with OpenSSL"
description: "A small shell loop to bruteforce unknown OpenSSL cipher and password combinations, plus using Hashcat rules to build the wordlist."
date: 2016-08-27
tags: [crypto, ctf, tooling]
---

Ever had to crack something without knowing the cipher? Sometimes the ciphertext hints at the algorithm, but not always. For those cases, this little script helps. Bruteforcing the cipher type might be the only way through a challenge. It produces a fair amount of data, but we can make that easier to process.

The scripts below take three inputs:

- A text file with all the ciphers OpenSSL supports (a list is at the bottom of this post).
- The password to guess, or a dictionary of passwords. The top 1000 common passwords is a reasonable dictionary.
- `encrypted.txt`, containing the ciphertext. If it holds base64 data, add the `-a` flag to the command.

Create a `cipherout` directory in your working directory first. The following command tries the passwords `CompanyName00` through `CompanyName99`:

```bash
while read -r line; do
  for i in {00..99}; do
    openssl $line -v -d -in encrypted.txt -pass pass:CompanyName$i -out cipherout/$line-$i.txt
    echo $line $i
  done
done < openssl-ciphers.txt
```

If you would rather guess from a wordlist, use a double loop:

```bash
while read -r line; do
  while read -r line2; do
    openssl $line -v -d -in encrypted.txt -pass pass:$line2 -out cipherout/$line-$line2.txt
    echo $line $line2
  done < wordlist.txt
done < ciphers.txt
```

This fills `cipherout` with one file per cipher-and-password combination. Analyze the folder for strings and alphanumeric output and see if anything makes sense. If you are working a challenge, remember the output could be yet another cipher.

You can also generate the guessing passwords with tooling. Hashcat does not crack these ciphers directly, since it is built for password hashes rather than encryption, but it makes a great wordlist generator. Build a small list of candidate passwords, then apply Hashcat's word-mangling rules. Applying the leetspeak rule to a wordlist containing `securesolutions` and `netsecurity` produces variations like:

```
hashcat64 --stdout /tmp/wordlist.txt -r /rules/leetspeak.rule
s3cur3solutions
securesolut1ons
secures0luti0ns
5ecure5olution5
$ecure$olution$
$3<ur3$0lut10n$
n3ts3curity
netsecur1ty
net5ecurity
ne7securi7y
n3t$3<ur1ty
```

### Quick list of OpenSSL ciphers

This may be missing some, depending on your OpenSSL build:

```
aes-128-cbc  aes-128-cfb  aes-128-ctr  aes-128-ecb  aes-128-gcm  aes-128-ofb
aes-192-cbc  aes-192-cfb  aes-192-ctr  aes-192-ecb  aes-192-gcm  aes-192-ofb
aes-256-cbc  aes-256-cfb  aes-256-ctr  aes-256-ecb  aes-256-gcm  aes-256-ofb
bf-cbc  bf-cfb  bf-ecb  bf-ofb  blowfish
camellia-128-cbc  camellia-192-cbc  camellia-256-cbc
cast5-cbc  cast5-cfb  cast5-ecb  cast5-ofb
des-cbc  des-cfb  des-ecb  des-ede3-cbc  des-ede3-cfb  des-ede3-ofb  desx-cbc
rc2-cbc  rc2-cfb  rc2-ecb  rc2-ofb  rc4  rc4-40
seed-cbc  seed-cfb  seed-ecb  seed-ofb
```
