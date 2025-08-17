day = int(input("Enter a number from 1 to 7 : "))
match day:
    case 1:
        print("Saturdy")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thursday")
    case 7:
        print("Friday")
    case _: # defult value using underscore(_)
        print("Invalid input")


# combine values
letter = input("Enter a letter : ").lower()
match letter:
    case "a" | "e" | "i" | "o"| "u":
        print("vowel")
    case _:
        print("consonant")


# If statement as guards
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

