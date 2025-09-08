num = int(input("Enter a number: "))

# Convert to string and check
if str(num) == str(num)[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
