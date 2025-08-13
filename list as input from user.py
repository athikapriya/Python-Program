n = input("Enter a number : ")
# 10 20 30
list = n.split()  # 10, 20, 20
sum = 0

for i in list:
    sum = sum + int(i)

print(sum)


# take a sentence as user input
# idendify how many words , digits, or letters are there

numOfLetters = 0
numOfWords = 0
numOfDigits = 0

text = input("Enter a text : ").lower()

for x in text:
    if x >= "a" and x <= "z":
        numOfLetters += 1
    elif x >= "0" and x <= "9":
        numOfDigits += 1
    elif x == " ":
        numOfWords += 1

if text.strip() != "":
    numOfWords += 1
print("Num of Letters : ", numOfLetters, ". Num of Words : ", numOfWords, ". Num of Digits : ",  numOfDigits)