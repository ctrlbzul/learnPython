import random

# function : border (garis lurus)
def printLine():
	print(f'------------------------------------------------------------')

# function : acak soal
def nomorSoal():
	return random.randint(1,3)

# list daftar soal
daftar_soal = ['Peribahasa yang memiliki makna \'kebaikan dibalas keburukan\' adalah...',
							 'Makna peribahasa \'bersatu kita teguh bercerai kita runtuh\' adalah...',
							 'Makna peribahasa \'besar pasak daripada tiang\'adalah...']

jawabanSoal1 = ['Air cucuran atap jatuhnya ke pelimbahan juga.',
								'Air susu dibalas dengan air tuba.',
								'Angkuh terbawa tampan tertinggal.']

jawabanSoal2 = ['Jika kita bersatu kita tidak akan runtuh.',
								'Sesuatu yang sebaiknya kita lakukan bersama.',
								'Sesuatu akan berhasil juga dilakukan secara bersama-sama.']

jawabanSoal3 = ['Hal yang tidak mungkin dilakukan.',
								'Pengeluaran lebih besar daripada pendapatan.',
								'Sesuatu yang tidak berguna dan bermanfaat.']

huruf_kuis = ['a', 'b', 'c']

# set soal dan jawaban
nomor = nomorSoal()
if nomor == 1:
	soal = daftar_soal[0]
	jawaban = jawabanSoal1
	kunci = 'b'
elif nomor == 2:
	soal = daftar_soal[1]
	jawaban = jawabanSoal2
	kunci = 'c'
elif nomor == 3:
	soal = daftar_soal[2]
	jawaban = jawabanSoal3
	kunci = 'b'

# generate soal untuk user
print(f'/ KUIS PERIBAHASA /')
printLine()
print(f'{soal}')
posisi_jawaban = random.sample(jawaban, 3)
for huruf, jawaban in zip(huruf_kuis, posisi_jawaban):
	print(f'{huruf}. {jawaban}')

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
