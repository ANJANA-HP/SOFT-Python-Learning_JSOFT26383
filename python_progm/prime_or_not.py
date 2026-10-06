a = int(input("Enter a number: "))
for x in range(2, a):
    if a % x == 0:
        print(a, "is not a prime number")
else:
    print(a, "is a prime number")
