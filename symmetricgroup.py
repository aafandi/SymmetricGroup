### Code to mimic the SymmetricGroup class in Sagemath ###

class SymmetricGroup:

    def __init__(self, n):
        self.order = n

    def __repr__(self):
        return f"The symmetric group on {self.order} elements"

    def __call__(self, list_of_tuples):
        # TODO: Make a call function where one can instantiate #
        # a permutation element

    def __mul__(self, other):
        # TODO: write a multiplication rule for two permutation elements #


### Run tests below ###




