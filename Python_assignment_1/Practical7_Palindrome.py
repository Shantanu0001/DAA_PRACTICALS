str=input("Enter the string to check palindrome: ")
str=str.casefold()

if(str==str[::-1]):
    print("Yes, it is palindrome.")
else:
    print("No, it is palindrome.")

    