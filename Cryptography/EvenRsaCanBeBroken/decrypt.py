from Crypto.Util.number import long_to_bytes, inverse

def decrypt():

		#-----------------------------------------
		# LANGKAH 1: Masukkan modulus N,e,c dari server
		#------------------------------------------
		N = 15565060413480483087540682654254276063993477696920225614084099260828443685896484161281676854071484475659792461191475516667663621290534685764123234514367938
		e = 65537
		c = 5953849932577836592747516748151794173565486006712279347558812691953222067777904343821677532874787335094655229671111342895274263866249163280394327964154595


		#-----------------------------------------
		# LANGKAH 2: Cek apakah modulus N genap 
		#------------------------------------------
		if N % 2 != 0:
			print("N ganjil, exploit ini tidak berlaku disini")
			return

			# ------------------------------------------------------------
			# LANGKAH 3: Faktorkan N
			# ------------------------------------------------------------
			# Karena N genap, dan satu-satunya prima genap adalah 2,
			# maka salah satu faktor prima N PASTI 2.

		else:
			p = 2
			q = N // 2

			print(f"p = {p}")
			print(f"q = {q}")

			# ------------------------------------------------------------
			# LANGKAH 4: Hitung phi(N) -- Euler's Totient
			# ------------------------------------------------------------
			# Rumus umum: phi(N) = (p - 1) * (q - 1)
			# Di sini p = 2, jadi (p - 1) = 1, sehingga:
			# phi(N) = 1 * (q - 1) = q - 1

			phi = (p - 1) * (q - 1)
			print("phi(N) =", phi)

			# ------------------------------------------------------------
			# LANGKAH 5: Hitung private exponent d
	    	# ------------------------------------------------------------
			# Definisi RSA: e * d = 1 (mod phi(N))
			# Artinya d adalah "invers modular" dari e, terhadap modulus phi(N).
			# pycryptodome punya fungsi siap pakai: inverse(a, n)

			d = inverse(e, phi)
			print("d =", d)

			# ------------------------------------------------------------
			# LANGKAH 6: Dekripsi ciphertext
			# ------------------------------------------------------------
			# Rumus dekripsi RSA: m = c^d mod N
			# pow(c, d, N) menghitung ini secara efisien (modular exponentiation)

			m = pow(c, d, N)

			# ------------------------------------------------------------
			# LANGKAH 7: Ubah angka m kembali jadi teks (flag)
			# ------------------------------------------------------------
			# Saat enkripsi, pesan (string) diubah dulu jadi angka besar
			# (bytes_to_long). Makanya sekarang dibalik pakai long_to_bytes.

			flag = long_to_bytes(m)
			print("\nFlag:", flag.decode(errors="ignore"))

decrypt()
