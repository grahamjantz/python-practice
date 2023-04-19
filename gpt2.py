import math

books = [89, 187, 78, 65, 62, 150, 31, 249, 250, 28]

def lcm(a, b):
    """Returns the least common multiple of two numbers a and b."""
    return a * b // math.gcd(a, b)

lcm_so_far = 1
for book_len in books:
    lcm_so_far = lcm(lcm_so_far, book_len)

day = lcm_so_far
while True:
    all_at_1 = True
    for book_len in books:
        if (day - 1) % book_len != 0:
            all_at_1 = False
            break
    if all_at_1:
        break
    day += 1

print("All books will reach chapter 1 on day", day)
