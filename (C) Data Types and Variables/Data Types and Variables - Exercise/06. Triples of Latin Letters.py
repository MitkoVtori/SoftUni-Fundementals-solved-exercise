number_of_letters = int(input())

for i in range(number_of_letters):
    for n in range(number_of_letters):
        for h in range(number_of_letters):
            print(f"{chr(97 + i)}{chr(97 + n)}{chr(97 + h)}")