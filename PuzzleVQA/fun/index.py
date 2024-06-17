import random

my_list = [10, 20, 30, 40, 50]
element_to_find = 30
print(my_list.index(element_to_find))  # 2

my_dict = {
    "apple": 5,
    "banana": 3, 
    "cherry": 8,
    "date": 2,
    "elderberry": 7
}
print(my_dict.keys())
print(type(my_dict.keys()))  # 返回值是个class，而不是list <class 'dict_keys'>
print(list(my_dict.keys()))  # ['apple', 'banana', 'cherry', 'date', 'elderberry']
key = random.choice(list(my_dict.keys()))
print(key, my_dict[key])