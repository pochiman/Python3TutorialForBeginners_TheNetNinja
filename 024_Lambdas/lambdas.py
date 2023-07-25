nums = [1,2,3,4,5,6]

def square(n):
    return n * n

lambda n: n * n  # inline anonymous functions and they're good when we only need to use a particular function once 
                 # so we can just use them in line within things like the map function or the filter function.

print(list(map(square, nums)))
print(list(map(lambda n: n * n, nums)))
