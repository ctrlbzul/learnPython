# import math module to get math.ceil() function
import math

# sequence of number from 1 until the value of d is found
i = 88
# e = public key and d = private key
e = 95
totient_n = 448 # ɸ(n)

# formula
print('i\t=', i)
print('ds\t= ceil((ɸ(n) * i)/e)')
print('ds\t= ceil((' + str(totient_n) + ' * ' + str(i) + '/' + str(e) + ')')

# ds = temporary value of d
float_ds = (totient_n * i)/e # get floating value of ds
round_ds = math.ceil(float_ds) # round up the float_ds to an integer
final_ds = (e*round_ds) % totient_n # get final value of ds

# print the result
print('\t= ceil(' + str(float_ds) + ') = ' + str(round_ds))
print('e * ds (mod ɸ (n)) = ', end='')
print(e, '*', round_ds, 'mod', e, '=', final_ds)
