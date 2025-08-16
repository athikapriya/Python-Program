vowels = "aeiou"
vowels_count = 0
consonant_count = 0

Word = input("Enter a Word: ")

for letter in Word:
    if letter in vowels :
        vowels_count += 1
    else:
        consonant_count += 1

print(f"Number of vowels: {vowels_count}." , end = " ")
print(f"Number of consonants: {consonant_count}")