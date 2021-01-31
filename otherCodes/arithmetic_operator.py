# online_shop

digitalWallet = 150000

# buying things
totalBuy = 65000
tax = totalBuy * 10 / 100

totalPrice = totalBuy + tax
change = digitalWallet - totalPrice

# print(text u want, variableName)
print("Digital Wallet : ", digitalWallet)
print("Total Buy      : ", totalBuy)
print("Tax            : ", tax)
print("Total Price    : ", totalPrice)
print("Change         : ", change)