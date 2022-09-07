print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

a = (lower_name1+lower_name2).count("t")
b = (lower_name1+lower_name2).count("r")
c = (lower_name1+lower_name2).count("u")
d = (lower_name1+lower_name2).count("e")
e = (lower_name1+lower_name2).count("l")
f = (lower_name1+lower_name2).count("o")
g = (lower_name1+lower_name2).count("v")
h = (lower_name1+lower_name2).count("e")

t=int(str(a+b+c+d)+str(e+f+g+h))

if t<10 or t>90:
  print(f"Your score is {t}, you go together like coke and mentos.")

elif t>40 and t<50:
  print(f"Your score is {t}, you are alright together.")
else:
 print(f"Your score is {t}.")

