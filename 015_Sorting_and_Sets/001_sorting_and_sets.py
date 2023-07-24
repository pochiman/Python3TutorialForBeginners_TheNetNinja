'''

>>> nums = [1,4,2,7,3,8,3,4,8,1]
>>> sorted(nums)
[1, 1, 2, 3, 3, 4, 4, 7, 8, 8]

>>> names = ['shaun', 'ryu', 'abe', 'Apple', 'Brian', 'shaun']
>>> sorted(names)
['Apple', 'Brian', 'abe', 'ryu', 'shaun', 'shaun']

>>> set(nums)  # removes duplicates and does not preserve order
{1, 2, 3, 4, 7, 8}

>>> set(names)
{'ryu', 'Apple', 'abe', 'Brian', 'shaun'}

>>> ninjas = {'ryu': 'black', 'yoshi': 'red', 'crystal': 'black'}
>>> ninjas.values()
dict_values(['black', 'red', 'black'])
>>> set(ninjas.values())
{'red', 'black'}

'''