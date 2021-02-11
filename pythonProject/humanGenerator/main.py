# import data.py
import data

# human generator
print('// Human Generator //')
name = input('Input a name\t\t: ')
gender = input('Input gender (M/F)\t: ')

# print all the human datas from data.py
print(
  f'''
  {data.printLine()}
  Name\t\t: {name}
  Gender\t: {data.getGender(gender)}
  Age\t\t: {data.getAge()}
  Hair Style\t: {data.getHairStyle(gender)}
  Head Shape\t: {data.getHeadShape()}
  Body Type\t: {data.getBodyType()}
  Country\t: {data.getCountry()}
  {data.printLine()}
  Data created on : {data.getCreatedTime()}
  ''')
