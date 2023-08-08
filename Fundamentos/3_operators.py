### Third Class ###

#Aritmetic Operators
print(1 + 1)
print(3 - 1)
print(2 * 2)
print(3 / 4)
print(10 % 2)
print(3 % 4)
print(2 ** 3)
print(10 // 2)#Division that always ends/aproximates to an Int
print("Hola" + " " + "Python")
#print("Hola" + 5) No funciona
print("Hola", str(5))
print(2 ** 3 + 3 - 7 / 1 // 4)
print("Hola " * 5)#Python has dynamic typing
print("Hola" * int(2.5))

#Comparative Operatos 
print(3 > 4, '3 > 4')
print(3 < 4, '3 < 4')
print(3 >= 4, '3 >= 4')
print(3 >= 3, '3 >= 3')
print(3 <= 4, '3 <= 4')
print(3 <= 3, '3 <= 3')
print(3 == 4, '3 == 4')
print(3 == 3, '3 == 3')
print(3 != 3, '3 != 3')
print(3 != 4, '3 != 4')
print(3 < 4 == 2, '3 < 4 == 2')
print(3 < 4 == 4, '3 < 4 == 4')
print('Hola' > 'Python', 'Hola > Python')
print('Hola' < 'Python', 'Hola < Python')
print('Hola' >= 'Python', 'Hola => Python')
print('Hola' <= 'Python', 'Hola <= Python')
print('Hola' == 'Python', 'Hola == Python')
print('Hola' != 'Python', 'Hola != Python')
print('Hola' > 'Sola', 'Hola > Sola')
print('Hola' >= 'Sola', 'Hola >= Sola')#Compares the alphabetic order

#Logic Operators
print(3 > 4 and "Hola" > "Python",'3 > 4 and Hola > Python')
print(3 > 4 or "Hola" > "Python", '3 > 4 or Hola > Python')
print(3 < 4 and "Hola" > "Python",'3 < 4 and Hola > Python')
print(3 > 4 or "Hola" < "Python", '3 > 4 or Hola < Python')
print(3 > 4 and "Hola" < "Python",'3 > 4 and Hola < Python')
print(3 < 4 or "Hola" > "Python", '3 < 4 or Hola > Python')
print(3 < 4 and "Hola" < "Python",'3 < 4 and Hola < Python')
print(3 > 4 or "Hola" > "Python", '3 > 4 or Hola > Python')
print(3 < 4 or ("Hola" > "Python" and 4 == 4), '3 < 4 or (Hola > Python and 4 == 4)')
#Not
print(not (3 > 4 and "Hola" > "Python"),'not(3 > 4 and Hola > Python)')
print(not(3 > 4) or "Hola" > "Python", 'not(3 > 4) or Hola > Python')
print(not(3 < 4 and "Hola" > "Python"),'not(3 < 4 and Hola > Python)')
print(3 > 4 or not("Hola" < "Python"), '3 > 4 or not(Hola < Python)')
print(not(3 > 4 and "Hola" < "Python"),'not(3 > 4 and Hola < Python)')
print(not(3 < 4 or "Hola" > "Python"), 'not(3 < 4 or Hola > Python)')
print(not(3 < 4 and "Hola" < "Python"),'not(3 < 4 and Hola < Python)')
print(not(3 > 4 or "Hola" > "Python"), 'not(3 > 4 or Hola > Python)')
print(not(3 < 4 or ("Hola" > "Python" and 4 == 4)), 'not(3 < 4 or (Hola > Python and 4 == 4))')