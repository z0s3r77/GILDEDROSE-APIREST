import pytest

from domain.items.Sulfuras import Sulfuras

"""
This module will check the legendary item sulfuras. And its quality behaviour.
"""


@pytest.fixture
def sulfur():
    test_sulfuras = Sulfuras("Sulfuras", 10, 80)

    return test_sulfuras


@pytest.mark.test_updateQuality
def test_updateQuality(sulfur):
    for i in range(0, 15):
        sulfur.updateQuality()

        assert sulfur.sell_in == 10
        assert sulfur.quality == 80
