import pytest
from StringUtils import StringUtils

@pytest.mark.parametrize('string, result', [("привет", "Привет"), ("test", "Test")])
def test_capitalize_positive(string, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("    Привет!", "Привет!"), ("       test", "test")])
def test_trim_positive(string, result):
    stringUtils = StringUtils()
    res = stringUtils.trim(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("а,б,в,г", ["а", "б", "в","г"])])
def test_to_list_positive(string, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("Скайпро", "С", True)])
def test_contains_positive(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("Скайпро", "У", False)])
def test_contains_positive(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("Скайпро", "о", "Скайпр"), ("Скайпро", "про", "Скай")])
def test_delete_symbol_positive(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("Скайпро", "С", True)])
def test_starts_with_positive(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("Скайпро", "о", False)])
def test_starts_with_negaitive(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("Скайпро", "о", True)])
def test_ends_with_positive(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [("Скайпро", "С", False)])
def test_ends_with_negative(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, result', [("", True), (" ", True)])
def test_is_empty_positive(string, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == result

@pytest.mark.parametrize('string, result', [("Скайпро", False), (".", False)])
def test_is_empty_negative(string, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [(["С", "к", "а", "й", "п", "р", "о"], ",", "С,к,а,й,п,р,о")])
def test_list_to_string_positive(lst, joiner, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(lst, joiner)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [([], "", "")])
def test_list_to_string_negative(lst, joiner, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(lst, joiner)
    assert res == result
