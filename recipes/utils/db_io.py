import re


units = ['g', 'mL', 'TBSP', 'tsp']


def parse_ingredients(s):
    '''
    Parses the ingredient NewRecipe form input to return list of ingredients.

    Parameters
    ----------
    s : str
        Input text from NewRecipe form.
    
    Returns
    -------
    ings = list of tuple
        List of ingredients as (name, quantity, unit).
    '''
    ings = []
    s_lines = s.split('\n')

    for line in s_lines:
        name = None
        quantity = None
        unit = None

        li = line.split()

        # any number at the beginning of the line will be stored as quantity
        q = re.search(r'\d+\.\d+|(?<=angle\s)\d+', li[0])
        if q:
            quantity = q[0]
            li.remove(li[0])

        # search list for strings that match any unit
        for x in li:
            if x in units:
                unit = x
                li.remove(x)
        
        # rest is ingredient name
        name = ' '.join(li)

        # add to ingredients list
        ings.append((name, quantity, unit))

