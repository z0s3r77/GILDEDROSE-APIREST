import pytest

from domain.items.Backstage import Backstage


@pytest.fixture
def store():
    item = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    return item

@pytest.mark.backstage
def test_backstage(store):

    '''
    We reate variables with the different states of the Backstage object
    over the days that are provided in the file report.txt
    '''

    dayOne      =   Backstage("Backstage passes to a TAFKAL80ETC concert", 14, 21)
    dayTwo      =   Backstage("Backstage passes to a TAFKAL80ETC concert", 13, 22)
    dayThree    =   Backstage("Backstage passes to a TAFKAL80ETC concert", 12, 23)
    dayFour     =   Backstage("Backstage passes to a TAFKAL80ETC concert", 11, 24)
    dayFive     =   Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 25)
    daySix      =   Backstage("Backstage passes to a TAFKAL80ETC concert", 9, 27)

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
