import pytest

@pytest.fixture
def fix_set():
    return {'I', 'like', 'python'}


# Проверка функции copy
def test_copy_fun(fix_return_set):
    new_set = fix_return_set.copy()
    assert new_set == fix_return_set


# Проверка функции remove
def test_remove_fun(fix_return_set):
    fix_return_set.remove('like')
    assert 'like' not in fix_return_set


# Проверка функции add
@pytest.mark.parametrize('add_param', ['test1', 'test2'])
def test_add_fun(fix_return_set, add_param):
    fix_return_set.add(add_param)
    assert add_param in fix_return_set


# Проверка пересечения множества
def test_inter_fun(fix_return_set):
    new_set = {'I', 'like', 'orange'}
    assert  fix_return_set.intersection(new_set) == {'I', 'like'}