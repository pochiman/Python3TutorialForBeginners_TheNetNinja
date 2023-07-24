'''

>>> ninja_belts = {"crystal": "red", "ryu": "black"}
>>> ninja_belts
{'crystal': 'red', 'ryu': 'black'}

>>> ninja_belts['crystal']
'red'

>>> ninja_belts['ryu']
'black'

>>> 'yoshi' in ninja_belts
False

>>> 'ryu' in ninja_belts
True

>>> ninja_belts.keys()
dict_keys(['crystal', 'ryu'])

>>> list(ninja_belts.keys())  # typecasting
['crystal', 'ryu']

>>> ninja_belts.values()
dict_values(['red', 'black'])
>>> vals = list(ninja_belts.values())
>>> vals
['red', 'black']
>>> vals.count('red')
1

>>> ninja_belts['yoshi'] = 'red'
>>> ninja_belts
{'crystal': 'red', 'ryu': 'black', 'yoshi': 'red'}

>>> person = dict(name="shaun", age=27, height="6ft")
>>> person
{'name': 'shaun', 'age': 27, 'height': '6ft'}

'''