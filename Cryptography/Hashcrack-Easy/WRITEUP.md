Hashcrack - EASY - Cryptography [CYBERLAB]

Deskripsi soal
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

Proses eksplorasi/recon
Login ke server dengan nc domain_server. Server memberikan hash password yang perlu di-crack untuk mendapat akses.

Insight kunci
Saya cek jenis hash dengan hashid hashed_password. hashid menampikan daftar kemungkinan algoritma yang dipakai untuk hash password awal saya mendapat tebakan MD2,MD4,MD5. Saya coba MD2 karena yang muncul pertama kali,kemungkinan cocok lebih besar
Langkah eksploitasi

1. Login ke server: nc domain_server
2. Identifikasi algoritma hash: hashid hashed_password
3. Ekstrak wordlist (kalau belum): cd /usr/share/wordlists/ lalu gunzip rockyou.txt.gz (perbaiki sesuai ekstensi file aslinya)
4. Crack hash: john --format=<algoritma> --wordlist=/usr/share/wordlists/rockyou.txt hash_file
5. Cek hasil crack: john --format=<algoritma> --show hash_file
6. Masukkan password yang berhasil ditebak ke server
7. Ulangi 1–6 sampai dapat flag

Flag
(isi setelah kamu jalanin ulang soalnya — jangan lupa dicatat langsung kali ini!)

Pelajaran

Hashcat versi terbaru kadang tidak support algoritma tertentu → John The Ripper jadi alternatif yang lebih stabil untuk kasus ini.
Nama format algoritma di JtR beda dengan nama umum, perlu hafal/cek referensi
