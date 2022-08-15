
from mimetypes import init


class NoDuplicates:

    def __init__(self, funct):
        self.funct = funct

    def __call__(self, cake, additives):
        no_duplicate_list = []
        for a in additives:
            print(f"additive added in call {a}")
            print(f"cake additives: {cake.additives}")
            if a not in cake.additives:
                print(f"cake doesn't contain {a}")
                no_duplicate_list.append(a)
                print(
                    f"list of all additives there are not in cake {no_duplicate_list}")
        self.funct(cake, no_duplicate_list)
