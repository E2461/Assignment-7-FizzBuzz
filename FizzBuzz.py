numbers = []
i = 1
while i < 101:
    numbers.append(i)
    i+=1
# print(numbers)

for j in numbers:
    if j % 5 == 0 and j % 3 == 0:
        print("FizzBuzz", sep="\n")
    elif j % 3 == 0:
        print("Fizz", sep="\n")
    elif j % 5 == 0:
        print("Buzz", sep="\n")
    else:
        print(j, sep="\n")
