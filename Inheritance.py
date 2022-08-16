from cgitb import text


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

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):

    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, _text):
        super().__init__(name, kind, taste, additives, filling)

        # occasion - okazja z jakiej jest zamawiany wypiek
        # shape - kształt tortu, np kwadratowy, piramida, jeż, standardowy
        # ornaments - dodatkowe ozdoby, np kwiatki, serduszka, listki
        # text - tekst jaki ma być wypisany na torcie

        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self._text = _text

    def show_info(self):
        super().show_info()
        print(f"Occasion - {self.occasion}\n", f"Shape - {self.shape}\n",
              f"Ornaments - {self.ornaments}\n", f"Text - {self._text}")


cake01 = SpecialCake('Vanilla Cake', 'cake', 'vanilla',
                     ['chocolade', 'nuts'], 'cream', 'Wedding', 'Circle', 'weird shapes on', 'Supper Wedding!')

cake01.show_info()
# cake02 = SpecialCake('Vanilla Cake', 'cake', 'vanilla',
#                      ['chocolade', 'nuts'], 'cream', 'Birthday')
