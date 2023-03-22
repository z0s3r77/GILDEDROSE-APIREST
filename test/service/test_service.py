import pytest
from service import service
from service.service import intializeDb, dropCollection

testItem = {
    "_id": 99999,
    "name": "+5 Dexterity Vest",
    "sell_in": 10,
    "quality": 20
}
sulfuras = {
    "_id": 888,
    "name": "Aged Brie",
    "sell_in": 0,
    "quality": 10
}


@pytest.mark.test_service
def test_initializeDb():
    success = intializeDb()
    assert success == True


@pytest.mark.test_service
def test_insert_item():
    assert service.insertItem(testItem) == "CREATED"
    assert service.insertItem(sulfuras) == "CREATED"


@pytest.mark.test_service
def test_insert_fail_item():
    assert service.insertItem('Not an item') == "ERROR"


@pytest.mark.test_service
def test_get_item():
    testItem = {
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20
    }
    assert service.getItem(99999) == testItem


@pytest.mark.test_service
def test_get_fail_item():
    result = {'name': '', 'quality': 0, 'sell_in': 0}
    assert service.getItem(733) == result


@pytest.mark.test_service
def test_update_item():
    service.updateItem(99999)
    resultItem = {
        "name": "+5 Dexterity Vest",
        "sell_in": 9,
        "quality": 18
    }
    assert service.getItem(99999) == resultItem


@pytest.mark.test_service
def test_update_AgedBrie_item():
    service.updateItem(888)
    resultAgedBrie = {
        "name": "Aged Brie",
        "sell_in": -1,
        "quality": 11
    }
    assert service.getItem(888) == resultAgedBrie


@pytest.mark.test_service
def test_getAllItems():
    allItems = service.getAllItems()
    assert len(allItems) >= 2


@pytest.mark.test_service
def test_updateAllItems():
    allItems = service.updateAllItems()
    assert len(allItems) >= 2


@pytest.mark.test_service
def test_delete_item():
    assert service.deleteItem(99999) == True
    assert service.deleteItem(888) == True


@pytest.mark.test_service
def test_delete_fail_item():
    assert service.deleteItem(12312323) == False
    dropCollection()
