import random

jawaban1 = ['Air cucuran atap jatuhnya ke pelimbahan juga.',
						'Air susu dibalas dengan air tuba.',
						'Angkuh terbawa tampan tertinggal.']

huruf = ['a', 'b', 'c']
posisi_jawaban = random.sample(jawaban1, 3)
for huruf, jawaban in zip(huruf, posisi_jawaban):
	print(f'{huruf}. {jawaban}')
