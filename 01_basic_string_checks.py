text = input("Enter a string: ")
if text.islower():  # All characters are lowercase 
    print("All lowercase")
elif text.isupper():  # All characters are uppercase
    print("All uppercase")
elif text.istitle():  # First character of each word is uppercase
    print("Title case")
elif text.isprintable():  # All characters are printable
    print("All printable characters")
elif text.isspace():  # Only whitespace characters
    print("Only whitespace")
elif text.isnumeric():  # All characters are numeric
    print("All numeric")

if text.isalpha():  # Only letters
    print("Only letters")
elif text.isalnum():  # Letters and numbers
    print("Alphanumeric")
elif text.isdigit():  # Only digits
    print("Only digits")
