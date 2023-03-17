import pytest
from service import crudMain


@pytest.mark.test_db
def test_get_item():
    itemToTest = (
        "[\n"
        "  {\n"
        '    "name": "+5 Dexterity Vest",\n'
        '    "sell_in": 10,\n'
        '    "quality": 20\n'
        "  }\n"
        "]"
    )
    assert crudMain.getItem("+5 Dexterity Vest") == itemToTest
