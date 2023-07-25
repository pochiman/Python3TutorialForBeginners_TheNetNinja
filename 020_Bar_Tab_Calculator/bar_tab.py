class Tab:

    menu = {
        'wine': 5,
        'beer': 3,
        'softdrink': 2,
        'chicken': 10,
        'beef': 15,
        'veggie': 12,
        'dessert': 6
    }

    def __init__(self):
        self.total = 0   # running total of the bill
        self.items = []  # list of items as we add them to the bill

    def add(self, item):
        self.items.append(item)  # We're adding the item to the list and also updating the total here with the cost of what they had.
        self.total += self.menu[item]  # This refers to the dictionary above where we wanna pass in a key which is gonna be the 
                                       # menu item and it's gonna return the value there and it's gonna add its value to the total.
    def print_bill(self, tax, service):
        tax = (tax / 100) * self.total
        service = (service / 100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20} £{self.menu[item]}')  # We're outputting the price of that particular item.

        print(f'{"Total":20} £{total:.2f}')

'''

Instructions:

cd 020_Bar_Tab_Calculator
> python

>>> from bar_tab import Tab     # We can create a new instance of a Tab now.
>>> table1 = Tab()              # Someone comes in and sits on table1 = new instance of a Tab.
>>> table1
<bar_tab.Tab object at 0x1084f0ad0>

>>> table1.add('softdrink')
>>> table1.add('chicken')
>>> table1.add('dessert')
>>> table1.print_bill(10, 10)   # We're passing in the tax and the service percentages.
softdrink            £2
chicken              £10
dessert              £6
Total                £21.20

'''