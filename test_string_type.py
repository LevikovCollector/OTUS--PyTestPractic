import pytest


# Проверка функции upper
@pytest.fixture
def fix_upper_string():
    return 'otus'.upper()


def test_upper_func(fix_upper_string):
    assert fix_upper_string == 'OTUS'

# Проверка конкатенации строк
@pytest.mark.parametrize('conc_param', ['python', 'world'])
def test_conc_func(conc_param):
    test_string = 'I like ' + conc_param
    if conc_param == 'python':
        assert test_string == 'I like python'
    else:
        assert test_string == 'I like world'


# Проверка среза
def test_slice_func():
    input_string = 'Hello World!'
    assert input_string[6:-1] == 'World'

# Проверка функции capitalize
def test_cap_func():
    input_string = 'otus'
    assert input_string.capitalize() == 'Otus'