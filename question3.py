n = int(input())

even_count = 0
odd_count = 0

for i in range(1, 11):
    result = n * i

    if result % 2 == 0:
        status = "Even"
        even_count += 1
    else:
        status = "Odd"
        odd_count += 1

    print(n, "x", i, "=", result, "-", status)

print("Even Results:", even_count)
print("Odd Results:", odd_count)
