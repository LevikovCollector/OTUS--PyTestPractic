import pytest

@pytest.fixture
def fix_dict():
    return { 'key1': 111,
             'key2': 222,
             'key3': 333
            }
# Проверка функции copy
def test_copy_func(fix_dict):
    new_dict = fix_dict.copy()
    assert new_dict == fix_dict

# Проверка функции update
@pytest.mark.parametrize('up_param', [{'key4': 444}, {'key5': 555}])
def test_update_func(fix_dict, up_param):
    item_key = list(up_param.keys())[0]
    item_val = up_param[item_key]
    fix_dict.update(up_param)

    assert fix_dict[item_key] == item_val

# Проверка функции get
def test_get_fun(fix_dict):
    assert fix_dict['key1'] == 111

#Проверка функции clear
def test_clear_fun(fix_dict):
    fix_dict.clear()
    assert fix_dict == {}