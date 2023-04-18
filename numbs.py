import sys

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


#89, 187, 78, 65, 62, 150, 31, 249, 250, 28

for item in total_books_list:
    book = []
    length_of_book = item[0]
    for i in range(length_of_book):
        book.append(i+1)
    item.append(book)
        
print("Thank you, calculating how long your reading cycle will be!")

master_list = []
complete = False
index = 0
day = 1
key = []

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

    # master_list.append(temp_list)
    
    if day % 100000 == 0 and day != 0:
        print(day, temp_list)

    if temp_list == key and index > 0:
        complete = True
        print('Cycle will complete on day:', str(day))
    
    # if day == 9000000:
    #     master_list = []
        
    

    index += 1
    day += 1


# master_index = 1
# for item in master_list:
#     if item == key and master_index > 1:
#         print('Cycle will complete on day', master_index)
#         years = round((master_index/365), 2)
#         print('This will take:', years, 'years to complete. Good luck!')
#     master_index += 1