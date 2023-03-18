import pytest
from service import crudMain


@pytest.mark.test_db
def test_get_item():

    result = {'name': '+5 Dexterity Vest', 'quality': 20, 'sell_in': 10}
    assert crudMain.getItem(1) == result
