# for n in range(5):
#     print(n)

# for n in range(3,10):
#     print(n)

# for n in range(0,20,4):
#     print(n)

burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n, burgers[n])

for n in range(len(burgers) -1, -1, -1):  # This will give me the index of the last item of the list.
    print(n, burgers[n])