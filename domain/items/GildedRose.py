from domain.items.NormalItem import NormalItem


class GildedRose:
    def __init__(self, items):
        self.items = items
        self.objects = []
        self.avaliableObjects = {
            "AgedBrie": "Aged Brie",
            "Sulfuras": "Sulfuras, Hand of Ragnaros",
            "Backstage": "Backstage passes to a TAFKAL80ETC concert",
            "Conjured": "Conjured Mana Cake"
        }

    def getObjects(self):
        return self.objects

    # Esta función nos crea una lista con los objetos de los items de Emily filtrados.
    # Aunque todos sean Items, en este codigo, se han hecho subclases por cada tipo de item
    # Esas subclases són los objetos disponibles en el diccionario self.avaliableObjects.
    def setObjects(self):
        for item in self.items:
            if item.name in self.avaliableObjects.values():
                for i in self.avaliableObjects:
                    if self.avaliableObjects[i] == item.name:
                        value = i
                self.objects.append([eval(value)(item.name, item.sell_in, item.quality)])
            else:
                self.objects.append([NormalItem(item.name, item.sell_in, item.quality)])

    def update_quality(self):
        for item in self.items:
            item[0].updateQuality()

