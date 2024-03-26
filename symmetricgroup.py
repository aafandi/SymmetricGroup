### Code to mimic the SymmetricGroup class in Sagemath ###

from itertools import permutations
from math import factorial


class SymmetricGroup:

    def __init__(self, n=1):
        self.order = n
        self.list_of_permutations = [permutation_to_cycles(perm) for perm in permutations(range(1, self.order + 1))]
        self.list_of_mappings = [cycles_to_mapping(perm, self.order) for perm in self.list_of_permutations]
        self.by_cycle_types = dictionary_of_cycle_types(self.order, self.list_of_permutations)

    def __repr__(self):
        return f"The symmetric group on {self.order} elements. This group has {factorial(self.order)} elements."
    

class Permutation:
    
    def __init__(self, order=1, cycles=[[]]):
        self.order = order
        self.cycles = cycles
        self.mapping = cycles_to_mapping(self.cycles, self.order)


    def __repr__(self):
        return (f"The permutation element that lives in the symmetric group on {self.order} elements, whose cycles are "
                f"{self.cycles}")


    def __mul__(self, other):
        if other.order != self.order:
            return "Those permutations can't be multiplied."
        else:
            product = product_of_mappings(self.mapping, other.mapping)
            cycles = mapping_to_cycles(product)
            return Permutation(self.order, cycles)


    def invert(self, as_cycles=False, as_mapping=True):
        ### Inverts a permutations ###

        inverted_mapping = {}

        for index in self.mapping:
            inverted_mapping[self.mapping[index]] = index

        if as_mapping:
            return inverted_mapping
        if as_cycles:
            return Permutation(self.order, mapping_to_cycles(inverted_mapping)).cycles




### Auxiliary Functions and Classes ###

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
        cycle = [domain_indices[0], mapping_dictionary[domain_indices[0]]]   # Initiation with the first two-cycle
        domain_indices.remove(domain_indices[0])                             # Delete from domain_indices
        while cycle[0] != cycle[-1]:                                         # Keep amending two-cycles, until
            cycle.append(mapping_dictionary[cycle[-1]])                      # you get back to the beginning of
            domain_indices.remove(cycle[-2])                                 # the cycle.
        list_of_cycles.append(cycle)                                         # Throw in the completed cycle

    for cycle in list_of_cycles:
        cycle.pop(-1) # Last index of the cycle is redundant

    return list_of_cycles


def cycles_to_mapping(pi, n):
    ### Takes a permutation pi (in the group S_n) ###
    ### in cycle notation, and returns the        ###
    ### dictionary {i: pi(i)}                     ###

    output = {}
    identity_elmt = {}

    for i in range(1, n + 1):
        identity_elmt[i] = i

    if pi == [[]]:
        return identity_elmt
    else:
        for cycle in pi:
            for i in range(len(cycle) - 1):
                output[cycle[i]] = cycle[i + 1]
            output[cycle[-1]] = cycle[0]
        for i in range(1, n + 1):
            if i not in output:
                output[i] = i



    return dict(sorted(output.items()))


def mapping_to_cycles(mapping_dictionary):
    ### Takes a mapping dictionary and returns the ###
    ### corresponding list of cycles               ###

    intermediary_permutation = []

    for i in mapping_dictionary:
        intermediary_permutation.append(mapping_dictionary[i])

    return permutation_to_cycles(intermediary_permutation)


def product_of_mappings(m1, m2):
    ### Takes two mapping dictionaries m1 and m2 ###
    ### and returns the product m1*m2 (first do  ###
    ### m1, then do m2).                         ###

    if len(m1) != len(m2):
        return "Those mappings can't be multiplied"
    else:
        output = {}
        for i in range(1, len(m1) + 1):
            output[i] = m2[m1[i]]
        return output


def cycle_type(n, list_of_cycles):
    ### Takes a permutation in S_n in cycle notation ###
    ### and returns its cycle type.                  ###

    if list_of_cycles == [[]]:
        return [1 for _ in range(n)]
    else:
        output = []
        non_trivial = 0
        for cycle in list_of_cycles:
            output.append(len(cycle))
            non_trivial += len(cycle)
        return output + [1 for _ in range(n - non_trivial)]


def dictionary_of_cycle_types(n, list_of_permutations):
    ### Takes a list of permutations and returns ###
    ### the dictionary {cycle_type:[perms]}      ###

    output = {}

    for perm in list_of_permutations:
        if tuple(cycle_type(n, perm)) in output:
            output[tuple(cycle_type(n, perm))].append(perm)
        else:
            output[tuple(cycle_type(n, perm))] = [perm]

    return output



###########################################
###########################################

### Run tests below ###





