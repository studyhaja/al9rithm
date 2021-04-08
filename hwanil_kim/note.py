def sum_digits(n):
    if n < 10:
        return n
    else:
        return int(str(n)[-1]) + sum_digits(int(str(n)[:-1]))


print(sum_digits(112))