import pytest
from context import db_io


@pytest.fixture
def ingredient_string():
    li = []

    li.append('1 Ei')
    li.append('500 g Kartoffeln')
    li.append('1 grüne Paprika')
    li.append('1 TBSP Paprika')
    li.append('1 Dose Tomaten')
    li.append('1 tsp Salz')
    li.append('gemahlener Pfeffer')

    s = '\n'.join(li)
    return s


@pytest.fixture
def ingredient_list():
    li = []

    # name, quantity, unit
    li.append(('Ei', '1', None))
    li.append(('Kartoffeln', '500', 'g'))
    li.append(('grüne Paprika', '1', None))
    li.append(('Paprika', '1', 'TBSP'))
    li.append(('Tomaten', '1', 'Dose'))
    li.append(('Salz', '1', 'tsp'))
    li.append(('gemahlener Pfeffer', None, None))

    return li

def test_parse_ingredients(ingredient_string, ingredient_list):
    
    s = ingredient_string
    li = ingredient_list

    li_test = db_io.parse_ingredients(ingredient_string)

    assert li == li_test
