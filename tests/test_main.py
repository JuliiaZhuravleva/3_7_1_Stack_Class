import pytest
from main import check_brackets


@pytest.mark.parametrize(
    'brackets, result', [
        ('(((([{}]))))', True),
        ('[([])((([[[]]])))]{()}', True),
        ('{{[()]}}', True),
        ('}{}', False),
        ('{{[(])]}}', False),
        ('[[{())}]', False)
    ]
)
def test_create_folder_status(brackets, result):
    res = check_brackets(brackets)
    assert res == result, f'Ошибка в последовательности {brackets}'
