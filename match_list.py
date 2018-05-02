# function of matching two lists
def match_list(a, b):
    """ find the indices of matching element 
    :param  a: list a 
            b: list b
    :return: The indices of elements in list a in list b 
    """
    return np.array([ b.index(x) if x in b else -1 for x in a ])

