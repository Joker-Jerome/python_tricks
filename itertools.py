import itertools
# ref
# https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8


data = [5, 2, 6, 4, 5, 9, 1]
result = itertools.accumulate(data, max)
for each in result:
    print(each)

shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for each in result:
    print(each)

shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations_with_replacement(shapes, 2)
for each in result:
    print(each)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
shapes = ['circle', 'triangle', 'square', 'pentagon']
result = itertools.chain(colors, shapes)
for each in result:
    print(each)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.dropwhile(lambda x: x<5, data)
for each in result:
    print(each)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = itertools.filterfalse(lambda x: x<5, data)
for each in result:
    print(each)

alpha_data = ['a', 'b', 'c']
result = itertools.permutations(alpha_data)
for each in result:
    print(each)

for i in itertools.repeat("spam", 3):
    print(i)
