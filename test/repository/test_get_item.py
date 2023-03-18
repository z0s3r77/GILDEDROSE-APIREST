import pytest
from service import service


@pytest.mark.test_db
def test_get_item():
    result = {"name": "+5 Dexterity Vest", "quality": 20, "sell_in": 10}
    assert service.getItem(1) == result
