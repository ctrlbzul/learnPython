# memanfaatkan fungsi math.ceil()
# untuk membulatkan bilangan ke atas
import math

e = 95 # e = public key dan d = private ke
totient_n = 448 # ɸ(n)

# ds = nilai d sementara, jika memenuhi syarat maka nilai ds menjadi nilai d.
# i	= urutan bilangan dimulai dari 1,2,3, dan seterusnya sampai nilai d ditemukan.
for i in range(1, 101):
  ds = math.ceil(((totient_n) * i) / e)
	# sisa, untuk menentukan apakah syarat untuk nilai d terpenuhi (0 ≤ d ≤ n)
  sisa = (e * ds) % totient_n
  
  print('Percobaan ke', i, ', sisa :', sisa)
  if sisa == 1:
    print('Syarat terpenuhi.')
    print('Jadi, nilai d =', ds)
    break
  else:
    print('Syarat tak terpenuhi!')
