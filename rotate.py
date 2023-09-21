import random

n = int(input("Hello, please enter length of array: "))
print("\nYou can either input your own array to be rotated or this can randomly generate one for you!")
rand_arr = input("\nWould you like to input your own array? (Y/N): ")

if (rand_arr.lower() == 'y'):
    rand_arr = False
elif (rand_arr.lower() == 'n'):
    rand_arr = True

rotate_deg = 0
while rotate_deg != 90 and rotate_deg != 180 and rotate_deg != 270:
    rotate_deg = int(input("How many degrees would you like to rotate? (90, 180, 270): "))

loops = int(rotate_deg / 90)

arr = []

if rand_arr == True:
    def generate_arr(length): 
        gen_arr = []
        for i in range(length): 
            tempArr = []
            for i in range(length):
                tempArr.append(random.randint(0, length - 1))
            gen_arr.append(tempArr)

        return gen_arr

    arr = generate_arr(n)
else:
    for i in range(0, n):
        tempArr = []
        for j in range(0, n):
            a = int(input("Input array number:"))
            tempArr.append(a)
            print(tempArr)
        arr.append(tempArr)
    

print("\nYour array before: ")
for i in range(len(arr)):
    print(arr[i])

def rotate(arr, rotations):
    master_arr = arr
    for x in range (0, rotations):
        final_arr = []
        for j in range(len(master_arr)):
            tempArr = []
            for i in range(len(master_arr)):
                tempArr.append(master_arr[i][j])
            rev_arr = list(reversed(tempArr))
            final_arr.append(rev_arr)
        master_arr = final_arr

    return final_arr

final_arr = rotate(arr, loops)

print("\nYour array after rotating ", rotate_deg, " degrees: ")
for i in range(len(final_arr)):
    print(final_arr[i])