def filter_out(first_list:list, target:int)-> list:
    new_list = []
    new_list = [number for number in first_list if number % target == 0 ]
    return new_list

b1 = filter_out([1, 2, 3, 4, 5, 33], 3)
print(b1)