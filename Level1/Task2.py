temp =float(input("Enter the temperature :"))
unit = (input("Enter the unit f or c: "))
c,f = 0,0
if unit == "f" or unit == "F":
   c = (temp - 32)*(5/9)
   print(c , "Celsius")

else:
   f = (temp*9/5)+32
   print(f  ,"Ferenheit")

