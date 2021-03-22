import random

# function : border (garis lurus)
def printLine():
	print(f'------------------------------------------------------------')

# function : acak soal
def nomorSoal():
	return random.randint(1,3)

# list daftar soal
daftar_soal = ['Peribahasa yang memiliki makna\'kebaikan dibalas keburukan\' adalah...',
							 'Makna peribahasa \'bersatu kita teguh bercerai kita runtuh\' adalah...',
							 'Makna peribahasa \'besar pasak daripada tiang\'adalah...']

# list daftar jawaban
daftar_jawaban = ['a. Air cucuran atap jatuhnya ke pelimbahan juga.\nb. Air susu dibalas dengan air tuba.\nc. Angkuh terbawa tampan tertinggal.',
									'a. Jika kita bersatu kita tidak akan runtuh.\nb. Sesuatu yang sebaiknya kita lakukan bersama.\nc. Sesuatu akan berhasil juga dilakukan secara bersama-sama.',
									'a. Hal yang tidak mungkin dilakukan.\nb. Pengeluaran lebih besar daripada pendapatan.\nc. Sesuatu yang tidak berguna dan bermanfaat.']

# set soal dan jawaban
nomor = nomorSoal()
if nomor == 1:
	soal = daftar_soal[0]
	jawaban = daftar_jawaban[0]
	kunci = 'b'
elif nomor == 2:
	soal = daftar_soal[1]
	jawaban = daftar_jawaban[1]
	kunci = 'c'
elif nomor == 3:
	soal = daftar_soal[2]
	jawaban = daftar_jawaban[2]
	kunci = 'b'

# generate soal untuk user
print(f'/ KUIS PERIBAHASA /')
printLine()
print(f'{soal}\n{jawaban}')

# jawaban dari user
jawaban_user = input('Jawaban anda : ')

# 3x gagal, kuis berakhir
kesempatan = 0
while True:
	# cek jawaban
	if jawaban_user == kunci:
		print(f'>> Jawaban anda benar ({kunci}).')
		break
	else:
		jawaban_user = input('Jawaban salah, coba lagi : ')
		kesempatan +=1
		if kesempatan == 3:
			print(f'>> Anda gagal.\ngitu aja gabisa tol aowawkwkw : {kunci}')
			break
