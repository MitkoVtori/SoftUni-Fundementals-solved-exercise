n = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"
my_list = []
filtered_numbers = []

for i in range(n):
    curr_num = int(input())
    my_list.append(curr_num)

command = input()

for num in my_list:
    filtered_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )

    if filtered_command:
        filtered_numbers.append(num)

print(filtered_numbers)