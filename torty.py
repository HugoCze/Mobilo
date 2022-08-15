cake_dict = {'cake_01': {'taste': 'vanilia',
                         'glaze': 'chocolade',
                         'text': 'Happy Brithday',
                         'weight': 0.7},
             'cake_02': {'taste': 'tee',
                         'glaze': 'lemon',
                         'text': 'Happy Python Coding',
                         'weight': 1.3}}


def show_cake_info(cake_dict):
    for key, value in cake_dict.items():
        print('{} cake with {} glaze with text "{}" of {} kg'.format(
            value["taste"], value["glaze"], value["text"], value["weight"]))


show_cake_info(cake_dict)


# Zmień go stosując następujące techniki:

# zmień definicję zmiennych na słownik z właściwościami

# zmień definicję funkcji, tak aby przyjmowała jeden parametr i nadal wyświetlała informacje przekazane parametrem

# utwórz listę tortów i przechodząc przez nią wyświetl informacje zwracane przez funkcje show_cake_info
