import pytest

from domain.items.Conjured import Conjured

"""
Test the class conjured
"""


@pytest.fixture
def conjured():
    test_conjur = Conjured("Conjured Cloth", 10, 30)

    return test_conjur


@pytest.mark.test_updateQuality
def test_updateQuality(conjured):
    check_quality = 30  # The quality starts at 30
    check_sell_in = 10
    # We make a loop to count 20 days and see if the quality is having a correctly behaviour
    for i in range(0, 20):
        # If the sellin is negative, decreases 4
        if check_sell_in < 0:
            check_quality -= 4

        # if the quality is negative, it returns to 0
        if check_quality < 0:
            check_quality = 0

        # Else if, the quality decreases 2
        elif check_sell_in >= 0:
            check_quality -= 2

        # We update de quality to the object
        conjured.updateQuality()
        check_sell_in -= 1

        # We compare if both qualities have the same behaviour
        assert conjured.quality == check_quality
        assert conjured.sell_in == check_sell_in
