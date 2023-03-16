from domain.items.NormalItem import NormalItem


class GildedRose:
    def __int__(self, items):
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
