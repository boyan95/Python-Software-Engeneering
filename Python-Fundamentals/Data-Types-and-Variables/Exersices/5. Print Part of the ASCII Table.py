ascii_start = int(input())
ascii_end = int(input())

for num in range (ascii_start, ascii_end + 1):
    print(f'{chr(num)} ', end ="")