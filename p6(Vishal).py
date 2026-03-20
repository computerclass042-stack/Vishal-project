# Advance calculator

print("Advanced Calculator")
print("1. Plus (+)")
print("2. Minus (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Square (x²)")
print("6. Square Root (√)")
print("7. Cube (x³)")
print("8. Cube Root (∛)")

choice = int(input("Enter choice (1-8): "))

# two number operations
if choice in [1,2,3,4]:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", a + b)

    elif choice == 2:
        print("Result =", a - b)

    elif choice == 3:
        print("Result =", a * b)
    
    elif choice == 4:
        if b == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result =", a / b)

# one number operations
elif choice in [5,6,7,8]:
    a = float(input("Enter number: "))

    if choice == 5:
        print("Result =", a ** 2)

    elif choice == 6:
        print("Result =", a ** (1/2))

    elif choice == 7:
        print("Result =", a * a * a)

    elif choice == 8:
        print("Result =", a ** (1/3))

else:
    print("Invalid choice")