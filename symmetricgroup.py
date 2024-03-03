### Code to mimic the SymmetricGroup class in Sagemath ###

class SymmetricGroup:

    def __init__(self, n):
        self.order = n

    def __repr__(self):
        return f"The symmetric group on {self.order} elements"

    def construct(self, list_of_tuples):
        return list_of_tuples


### Run tests below ###

G = SymmetricGroup(3); print(G.construct([(1,), (2,)]))
