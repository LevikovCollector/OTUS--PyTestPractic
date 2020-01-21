import pytest


@pytest.fixture
def fix_dict():
    return {'key1': 111,
            'key2': 222,
            'key3': 333
            }


def test_copy_func(fix_dict):
    '''Проверка функции copy '''
    new_dict = fix_dict.copy()
    assert new_dict == fix_dict


@pytest.mark.parametrize('up_param', [{'key4': 444}, {'key5': 555}])
def test_update_func(fix_dict, up_param):
    '''Проверка функции update '''
    item_key = list(up_param.keys())[0]
    item_val = up_param[item_key]
    fix_dict.update(up_param)

    assert fix_dict[item_key] == item_val


def test_get_fun(fix_dict):
    '''Проверка функции get'''
    assert fix_dict['key1'] == 111


def test_clear_fun(fix_dict):
    '''Проверка функции clear'''
    fix_dict.clear()
    assert fix_dict == {}


def test_values_fun(fix_dict):
    '''Проверка функции values'''
    val_dict = list(fix_dict.values())
    assert val_dict == [111, 333, 222]
