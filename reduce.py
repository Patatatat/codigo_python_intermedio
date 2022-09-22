from functools import reduce


my_list = [2, 2, 2, 2, 2]

all_multiplied = reduce(lambda x, y: x*y, my_list)

print(all_multiplied)