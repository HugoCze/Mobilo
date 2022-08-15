import pickle
import glob
import types


class Cake:

    bakery_offer = []
    known_types = ['cake', 'muffin', 'meringue', 'biscuit',
                   'eclair', 'christmas', 'pretzel', 'other']

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        self.kind = kind
        if self.kind not in Cake.known_types:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__gluten_free = gluten_free
        self.__text = text

        Cake.bakery_offer.append(self)

    def show_info(self):

        print(self.name.upper())
        print(f"Taste: {self.taste}")
        print(f"Kind: {self.kind}")
        if len(self.additives) > 0:
            print(f" Additives:\n {str(self.additives)}")
        if len(self.filling) > 0:
            print(f"Filling: {self.filling}")
        print(f" Gluten free: {self.__gluten_free}")
        print(f"Text to display: {self.__text}")
        print("---------------------")

    def set_filling(self, filling):
        self.filling = filling

    def set_additives(self, additives):
        self.additives.append(str(additives))

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == "cake" or new_text == "":
            self.__text = new_text
            print(f"Changing text to {new_text}")
        else:
            print(
                f"Changing text to {new_text} is impossible as kind is {self.kind}\n an only 'cake' is valid kind to text")

    def save_to_file(self, path):
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as f:
            new_cake = pickle.load(f)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files():
        list_of_files = []
        files = glob.glob("*.bakery")
        list_of_files.append(files)
        return list_of_files

    SetANewText = property(__get_text, __set_text, None,
                           'Assign new text to Cake class object')


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(
            obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


sernik = Cake("sernik", "cake", "serowy na słodko",
              "lukier", "", True, "Happy Birthday!")
babeczki = Cake("Muffiny", "pieczone ciasto", "truskawkowy",
                ["krem kawowy"], "czekoladowy", False, "")
brownie = Cake("Brownie", "cake", "czekoladowy-brownie",
               ["cukier puder", ], "", False, "Lucky cupcake!")
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, "")

cakes_list = [cake04, brownie, babeczki, sernik]


def export_all_cakes_to_html(cls, path):
    template = """
    <table border=1>
        <tr>
        <th colspan=2>{}</th>
        </tr>
        <tr>
            <td>Kind</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Taste</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Additives</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Filling</td>
            <td>{}</td>
        </tr>
    </table>"""
    with open(path, "w") as f:
        for cake in cls.bakery_offer:
            cake = template.format(
                cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
            f.write(cake)


# sernik = Cake("sernik", "cake", "serowy na słodko",
#               "lukier", "", True, "Happy Birthday!")
# babeczki = Cake("Muffiny", "pieczone ciasto", "truskawkowy",
#                 ["krem kawowy"], "czekoladowy", False, "")
# brownie = Cake("Brownie", "cake", "czekoladowy-brownie",
#                ["cukier puder", ], "", False, "Lucky cupcake!")
# cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, "")

# export_1_cake_to_html(sernik, r"sernik.html")
Cake.Export_All_Cakes = types.MethodType(export_all_cakes_to_html, Cake)
Cake.Export_All_Cakes(path=r"cakes.html")
# sernik.SetANewText = "Nowy napis na serniku"
# babeczki.SetANewText = "Nowy napis na babczkach"
# brownie.SetANewText = "Nowy napis na brownie"
# cake04.SetANewText = "Nowy napis na na ciastku 04"

# sernik.save_to_file("sernik.bakery")
# cake04.save_to_file("cake04.bakery")
# sernik.read_from_file("sernik.bakery")
# print(sernik.get_bakery_files())
# print("Today in our offer:")
# for cake in Cake.bakery_offer:
#     cake.show_info()
