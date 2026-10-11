num = 90517
digits_sum = 0

while num > 0:
    digits_sum += num % 10
    num //= 10

print(digits_sum)
