# for x in range(1, 11):
#     print(' ' * (10 - x) + '*' * (2 * x - 1))

# for x in range(9, 0, -1):
#     print(' ' * (10 - x) + '*' * (2 * x - 1))

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)