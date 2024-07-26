import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '|', '~', '@', '^', '=', '[', ']','{', '}']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
mylist = []
final = ''
i = 1
j = 1
k = 1
while i<=nr_letters:
  x = random.choice(letters)
  mylist.append(x)
  i += 1
while j<=nr_numbers:
  y = random.choice(numbers)
  mylist.append(y)
  j += 1
while k<=nr_symbols:
  z = random.choice(symbols)
  mylist.append(z)
  k += 1
random.shuffle(mylist)

for i in range(len(mylist)):
  final = final + mylist[i]
print(final)