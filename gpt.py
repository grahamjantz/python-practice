import math

books = [89, 187, 78, 65, 62, 150, 31, 249, 250, 28]

def lcm(a, b):
    """Returns the least common multiple of two numbers a and b."""
    return a * b // math.gcd(a, b)

lcm_so_far = 1

for book_len in books:
    lcm_so_far = lcm(lcm_so_far, book_len)

day = lcm_so_far
for i, book_len in enumerate(books):
    day -= (day - i - 1) % book_len - 1

print("All books reached chapter 1 on day", day)
