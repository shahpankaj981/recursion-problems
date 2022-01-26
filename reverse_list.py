def reverse_list(l):
    print(l)
    if len(l) == 0: return []
    return [l[-1]] + reverse_list(l[:-1])

original_list = [1,2,3,4,5]
print("reverse list is:", reverse_list(original_list))
