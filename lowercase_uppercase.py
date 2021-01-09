# lambda arguments: expression 
toUpperCase = lambda x: x.upper() 
toLowerCase = lambda x: x.lower()

print("[ Upper case and Lower case Generator ]")
print("[ 1.To Upper Case     2.To Lower Case ]")
print("=======================================")

txt = str(input("Paste/type your text here : "))

choose = str(input("Choose generator (1/2) :"))
if choose == "1":
	print(toUpperCase(txt))
elif choose == "2":	
	print(toLowerCase(txt))
else:
	print("ERROR : Only choose 1 or 2!")
