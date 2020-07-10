a = [[1,2], [2,1]]

# keeping orders
b = [list(x) for x in set(tuple(x) for x in a)]
# not keeping orders
c = [list(x) for x in set(tuple(set(x)) for x in a)]
