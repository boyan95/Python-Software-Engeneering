subs = input().split(", ")
test_list = input().split(", ")
"""
res = [subs for subs in substrings for word in words if subs in word]
print(sorted(set(result), key= result.index))
"""
res = []
for el in subs:
    for i in test_list:
        if el in i:
            res.append(el)
            break
print(res)
