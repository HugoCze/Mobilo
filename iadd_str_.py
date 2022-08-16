class Cake:

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)

    def __str__(self):
        return f"Printed object: name: {self.name}, kind: {self.kind}, additives: {self.additives}"

    def __iadd__(self, new_items):
        if type(new_items) is list:
            additives = self.additives
            additives.extend(new_items)
            return Cake(self.name, self.kind, self.taste, additives, self.filling)
        elif type(new_items) is str:
            additives = self.additives
            additives.append(new_items)
            return Cake(self.name, self.kind, self.taste, additives, self.filling)
        else:
            raise Exception(
                f'Adding type {type(new_items)} to Cake is not implemented.')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla',
              ['chocolade', 'nuts'], 'cream')
cake01.show_info()

cake01 += ['magic stars', 'More chocolate']
cake01.show_info()
