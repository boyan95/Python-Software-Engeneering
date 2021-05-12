data = input().split("\\")
result = data[-1].split(".")
print(f"File name: {result[0]}\nFile extension: {result[1]}")