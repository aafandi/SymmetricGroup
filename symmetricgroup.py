### Code to mimic the SymmetricGroup class in Sagemath ###

from itertools import permutations
from math import factorial

class SymmetricGroup:

    def __init__(self, n):
        self.order = n

    def __repr__(self):
        return f"The symmetric group on {self.order} elements"

    def __call__(self, list_of_tuples):
        # Makes a call function where one can instantiate #
        # a permutation element
        return list_of_tuples

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

def permutation_to_cycles(t):
    ### Function that takes a tuple (\pi(i)), corresponding ###
    ### to some permutation, and returns the permuutation   ###
    ### in cycle notation, as a list of tuples              ###

    input_to_list = []        # Turn input tuple to list
    mapping_dictionary = {}   # The dictionary {i:pi(i)}, EXCLUDES FIXED POINTS
    domain_indices = []       # List keeping track of beginning of two-cycles
    list_of_cycles = []       # Desired output


    for i in t:
        input_to_list.append(i)

    for input_output_pair in zip([i for i in range(1, len(t) + 1)], input_to_list):
        if input_output_pair[0] != input_output_pair[1]:
            mapping_dictionary[input_output_pair[0]] = input_output_pair[1]

    for i in mapping_dictionary:
        domain_indices.append(i)

    while len(domain_indices) > 0:
        cycle = [domain_indices[0], mapping_dictionary[domain_indices[0]]]
        domain_indices.remove(domain_indices[0])
        while cycle[0] != cycle[-1]:
            cycle.append(mapping_dictionary[cycle[-1]])
            domain_indices.remove(cycle[-2])
        list_of_cycles.append(cycle)

    for cycle in list_of_cycles:
        cycle.pop(-1)

    return list_of_cycles




### Run tests below ###

for perm in permutations([1, 2, 3, 4]):
    print(perm, permutation_to_cycles(perm))



