import re


accepted_units = ['g', 'kg', 'l', 'ml']


def parse_ingredients(text):
    '''
    Parse text entered in form for ingredients, return ingredient, quantity, unit.

    Arguments
    ---------
    text : str
        Text from recipe form for ingredients.

    Returns
    -------
    ingredients : list
        List of tuples (ingredient, quantity, unit).
    '''
    ingredients = []

    elements = text.split('\n')
    elements = [x for x in elements if x != '']
    for line in elements:
        re_q = re.search(r'((\d+(\.\d+)?)|(\.\d+))', line)
        if re_q:
            quantity = float(re_q.group(0))
            if quantity.is_integer():
                quantity = int(quantity)
        else:
            quantity = None

        re_x = re.findall(r'[a-zA-ZäöüßÄÖÜ]+', line)
        if re_x[0] in accepted_units:
            unit = re_x[0]
            re_x.remove(unit)
        else:
            unit = 'piece'

        ingredient = ' '.join(re_x)

        ingredients.append((ingredient, quantity, unit))

    return ingredients
