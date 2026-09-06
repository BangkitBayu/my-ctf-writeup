#-------------------------------------------
#   Import library yang dibutuhkan
#-------------------------------------------

import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

#---------------------------------------------
#   Masukkan ciphertext dan timestamp dari message.txt
#--------------------------------------------
ciphertext_hex = "2bcf79055a60b74654fada617a98a6f05bccbed9c2c9d74144f564fa699c6df3"
ciphertext_bytes = bytes.fromhex(ciphertext_hex) #Ubah dari hex ke bytes

timestampClue = 1770242628

#---------------------------------------------
#  Fungsi untuk generate ulang keynya
#--------------------------------------------
def make_key(timestamp):
	return hashlib.sha256(str(timestamp).encode()).digest()[:16]

#---------------------------------------------
#   Fungsi untuk mencoba deskripsi
#--------------------------------------------
def try_decrypt(timestamp, ciphertext_bytes):
	key = make_key(timestamp)
	cipher = AES.new(key, AES.MODE_ECB)

	try:
		decrypted = cipher.decrypt(ciphertext_bytes)
		plaintext = unpad(decrypted, AES.block_size)
		return print(plaintext)
	except (ValueError, KeyError):
		return None

try_decrypt(timestampClue, ciphertext_bytes)