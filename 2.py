numbers = []
while True:
    number = (input("Enter a number(enter at least 5 numbers):"))
    if number == "":
        break
    numbers.append(float(number))
numbers.sort(reverse=True)
print("The five greatest numbers are:")
for number in numbers[:5]:
    print(number)