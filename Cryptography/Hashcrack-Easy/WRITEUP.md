# Hashcrack - EASY - Cryptography [PICOCTF]

## Deskripsi soal
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

## AHA Momment
Saya cek jenis hash dengan hashid hashed_password. hashid menampikan daftar kemungkinan algoritma yang dipakai untuk hash password awal saya mendapat tebakan MD2,MD4,MD5. Saya coba MD2 karena yang muncul pertama kali,kemungkinan cocok lebih besar

## Langkah-langkah
1. Login ke server: nc domain_server
2. Identifikasi algoritma hash: hashid hashed_password
3. Ekstrak wordlist (kalau belum): cd /usr/share/wordlists/ lalu gunzip rockyou.txt.gz (perbaiki sesuai ekstensi file aslinya)
4. Crack hash: john --format=<algoritma> --wordlist=/usr/share/wordlists/rockyou.txt hash_file
5. Cek hasil crack: john --format=<algoritma> --show hash_file
6. Masukkan password yang berhasil ditebak ke server
7. Ulangi 1–6 sampai dapat flag

```
Flag
```
