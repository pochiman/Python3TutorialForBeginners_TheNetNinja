my_name = 'ryu'  # global scope

def print_name():
    global my_name  # overriding the global variable
    my_name = 'yoshi'  # local scope
    print('the name inside the function is', my_name)

print_name()
print('outside the function the name is', my_name)
