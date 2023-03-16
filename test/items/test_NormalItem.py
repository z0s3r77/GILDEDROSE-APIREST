import pytest

from domain.items.NormalItem import NormalItem


@pytest.fixture
def store():
    item = NormalItem("+5 Dexterity Vest", 10, 20)
    return item

@pytest.mark.normalItem
def test_normalItem(store):

    '''
    We reate variables with the different states of the normal object
    over the days that are provided in the file report.txt
    '''

    dayOne      =   NormalItem("+5 Dexterity Vest", 9, 18)
    dayTwo      =   NormalItem("+5 Dexterity Vest", 8, 16)
    dayThree    =   NormalItem("+5 Dexterity Vest", 7, 14)
    dayFour     =   NormalItem("+5 Dexterity Vest", 6, 12)
    dayFive     =   NormalItem("+5 Dexterity Vest", 5, 10)
    daySix      =   NormalItem("+5 Dexterity Vest", 4, 8)

    '''
    we update once for each day it spends in the inventory 
    and check that it matches the result of the report.txt
    '''
    # update Day 1
    store.updateQuality()
    assert repr(store) == repr(dayOne)

    # update Day 2
    store.updateQuality()
    assert repr(store) == repr(dayTwo)

    # update Day 3
    store.updateQuality()
    assert repr(store) == repr(dayThree)

    # update Day 4
    store.updateQuality()
    assert repr(store) == repr(dayFour)

    # update Day 5
    store.updateQuality()
    assert repr(store) == repr(dayFive)

    # update Day 6
    store.updateQuality()
    assert repr(store) == repr(daySix)