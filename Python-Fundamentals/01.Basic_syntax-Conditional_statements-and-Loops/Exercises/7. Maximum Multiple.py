divisor = int(input())
bound = int(input())

for n in range(bound, divisor, -1):
    if 0 < n <= bound and n % divisor == 0:
        print(n)
        break
