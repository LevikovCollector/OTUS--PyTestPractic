import pytest


@pytest.fixture
def fix_upper_string():
    return 'otus'.upper()


def test_upper_func(fix_upper_string):
    '''Проверка функции upper'''
    assert fix_upper_string == 'OTUS'


@pytest.mark.parametrize('conc_param', ['python', 'world'])
def test_conc_func(conc_param):
    '''Проверка конкатенации строк'''
    test_string = 'I like ' + conc_param
    if conc_param == 'python':
        assert test_string == 'I like python'
    else:
        assert test_string == 'I like world'


def test_slice_func():
    '''Проверка среза'''
    input_string = 'Hello World!'
    assert input_string[6:-1] == 'World'


def test_cap_func():
    '''Проверка функции capitalize'''
    input_string = 'otus'
    assert input_string.capitalize() == 'Otus'


def test_split_func():
    '''Проверка функции split'''
    input_string = 'I like python'
    assert input_string.split(' ') == ['I', 'like', 'python']
