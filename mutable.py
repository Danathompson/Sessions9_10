lst = [1, 3, 5, 7, 9]
lst[1]
3
lst[1] = 11
print(lst)
[1, 11, 5, 7, 9]
lst[1] = lst[2]
print(lst)
[1, 5, 5, 7, 9]
lst[6] = 10