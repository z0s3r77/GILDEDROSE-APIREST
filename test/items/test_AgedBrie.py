from src.gilded_rose import *
import pytest

'''
Unitary test to check if Aged Brie quality has the correct behaviour
'''


# Using a fixture to interact correctly with the class AgedBrie
@pytest.fixture
def cheese():
    test_cheese = AgedBrie("Cheese", 5, 10)

    return test_cheese


# Test the method that update the quality of the class AgedBrie adapted to its category.
@pytest.mark.test_updateQuality
def test_updateQuality(cheese):
    check_quality = 10
    check_sell_in = 5

    for i in range(0, 12):

        # If the sellin is positive, increase 1
        if check_sell_in >= 0:
            check_quality += 1

        # if the quality is negative, it returns to 0
        if check_quality < 0:
            check_quality = 0

        # Else if the sell in date has passed, the quality increases 2
        elif check_sell_in < 0:
            check_quality += 2

        # We update de quality to the object
        cheese.updateQuality()
        check_sell_in -= 1
        assert cheese.sell_in == check_sell_in
        assert cheese.quality == check_quality