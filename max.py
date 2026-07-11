# The bottom three lines take numbers from the input.
a = int(input("number1: "))
b = int(input("number2: "))
c = int(input("number3: "))

# The lower bets check which number is greater or equal.
if a == b == c:
    print("Equal")
elif a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    print(b)
else:
    print(c)
