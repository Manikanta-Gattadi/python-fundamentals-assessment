text = input("Enter a string: ")
count = 0
for char in text:
    if char.lower() in "aeiou":
        count = count + 1
print("Total number of vowels:", count)
