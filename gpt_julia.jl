books = [89,187,78,65,62,150,31,249,250,28]

function lcm(a, b)
    """Returns the least common multiple of two numbers a and b."""
    return a * b / gcd(a, b)
end

lcm_so_far = 1
for book_len in books
    lcm_so_far = lcm(lcm_so_far, book_len)
end

day = lcm_so_far
while true
    all_at_1 = true
    for book_len in books
        if rem(day - 1, book_len) != 0
            all_at_1 = false
            break
        end
    end
    if all_at_1
        break
    end
    day += 1
end

println("All books will reach chapter 1 on day ", day)
