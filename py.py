import csv

def reading_generator(name, length):
    chapters = []
    
    index = 1

    while index <= length:
        daily_reading = name + " " + str(index)
        chapters.append(daily_reading)
        index += 1
    
    file_name = name.lower() + '.csv'

    with open(file_name,'w', newline='') as reading:
        fields = ['Reading'] 
        writer = csv.DictWriter(reading, fieldnames=fields)
        for item in chapters:
            writer.writerow({'Reading': str(item)})


bible_books = [
    ['Genesis', 50],
    ['Exodus', 40],
    ['Matthew', 28]
]

for book in bible_books:
    reading_generator(book[0], book[1])