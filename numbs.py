import sys

# 89 187 78 65 62 150 31 249 250 28

cli_arguments = sys.argv

total_books_list = []

if len(cli_arguments) > 1:
    for i in cli_arguments[1:]:
        tmp_list_cli = []
        tmp_list_cli.append(int(i))
        total_books_list.append(tmp_list_cli)
        
else:
    total_books = int(input("How many books are you wanting to read? "))

    for i in range(total_books):
        tmp_list = []
        print("How many chapters is book", i+1, "?")
        length = int(input(" "))
        tmp_list.append(length)
        total_books_list.append(tmp_list)



for item in total_books_list:
    book = []
    length_of_book = item[0]
    for i in range(length_of_book):
        book.append(i+1)
    item.append(book)
        
print("Thank you, calculating how long your reading cycle will be!")

complete = False
# index = 0 + 1000000000
# day = 1 + 1000000000
index = 0 
day = 1
key = []

# 1500000 [83, 73, 60, 60, 34, 150, 30, 24, 250, 12]
# 1500000 [83, 73, 60, 60, 34, 150, 30, 24, 250, 12]

# numbs.py ran on my phone for this many cycles with no match. tested running program starting at 100,000 less than this value and it produced the same temp_list value so it works to add to the index and day values to 'skip' ahead in the program running to get closer to the answer see down VVVV
# 896600000 [27, 76, 62, 10, 20, 50, 20, 53, 250, 16]
# 896600000 [27, 76, 62, 10, 20, 50, 20, 53, 250, 16]

for i in total_books_list:
    key.append(1)

while complete == False:
    temp_list = []

    def add_to_temp(input_list):
        tmp_index = index

        if tmp_index >= len(input_list):
            tmp_index %= len(input_list) 
            temp_list.append(input_list[tmp_index])
        else:
            temp_list.append(input_list[tmp_index])

    for i in total_books_list:
        add_to_temp(i[1])

    if day % 251 == 0 and day != 0:
        print(day, temp_list)

    if temp_list == key and index > 0:
        complete = True
        print(temp_list)
        print('Cycle will complete on day:', str(day))
        years = round((day/365), 2)
        print('This will take:', years, 'years to complete. Good luck!')
 
    index += 11640750
    day += 11640750
