### Code to mimic the SymmetricGroup class in Sagemath ###

class SymmetricGroup:

    def __init__(self, n):
        self.order = n

    def __repr__(self):
        return f"The symmetric group on {self.order} elements"

    def __call__(self, list_of_tuples):
        # TODO: Make a call function where one can instantiate #
        # a permutation element
        pass

    def __mul__(self, other):
        # TODO: write a multiplication rule for two permutation elements #

        pass

def cycles_to_dict(l):
    ### Takes a permutation pi in cycle notation, and returns ###
    ### the dictionary {i: pi(i)}                             ###

    d = {}

    for cycle in l:
        if len(cycle) == 1:
            d[cycle[0]] = cycle[0]
        else:
            for i in range(len(cycle) - 1):
                d[cycle[i]] = cycle[i + 1]
            d[cycle[-1]] = cycle[0]

    return d

def dict_to_cycles(d):
    ### Takes the dictionary {i: pi(i)} and returns the ###
    ### corresponding list of cycles                    ###

    pass




def multiply_permutations(p1, p2):
    ### Takes two permutations, p1 and p2, presented in ###
    ### cycle notation, as lists of tuples, and returns ###
    ### their product, also as a list of tuples         ###


    d1 = cycles_to_dict(p1)
    d2 = cycles_to_dict(p2)

    product = {}

    for i in range(1, len(d1) + 1):
        product[i] = d2[d1[i]]

    return product





### Run tests below ###

a = [(1, 2, 3), (5, 4, 6)]
b = [(2, 5), (4, 6), (1, 3)]

print(multiply_permutations(a, b))


