class GildedRose:
    def __init__(self, items):
        self.items = items
        self.objects = []
        self.avaliableObjects = {
            "AgedBrie": "Aged Brie",
            "Sulfuras": "Sulfuras, Hand of Ragnaros",
            "Backstage": "Backstage passes to a TAFKAL80ETC concert",
            "Conjured": "Conjured Mana Cake",
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
                self.objects.append(
                    [eval(value)(item.name, item.sell_in, item.quality)]
                )
            else:
                self.objects.append([NormalItem(item.name, item.sell_in, item.quality)])

    def update_quality(self):
        for item in self.items:
            item[0].updateQuality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def getName(self):
        return self.name

    def getSell_in(self):
        return self.sell_in

    def getQuality(self):
        return self.quality

    def setQuality(self, valor):
        self.quality = valor

    # Esto es un recurso Pythonico
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Por cumplir con los contratos de Java
class Interfaz:
    def updateQuality():
        pass


class NormalItem(Item, Interfaz):
    # Aquí se establece que NormalItem es un tipo de Item
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    # Cada vez que se ejecuta un updateQuality, se resta 1 a un NormalItem
    def setSell_in(self):
        self.sell_in = self.sell_in + -1

    # Calculamos la calidad de un NormalItem
    def computeQuality(self, valor):
        if self.quality + valor > 50:
            self.setQuality(50)

        elif self.quality + valor >= 0:
            self.setQuality(self.getQuality() + valor)

        else:
            self.setQuality(0)

    # Actualizamos la calidad de un NormalItem, primero vemos si se ha caducado o no
    # En base a esto se eligirán una de las dos opciones.
    # Después como se ha actualizado la calidad, significa que ha pasado un día y se ejecuta setSell_In
    # Así interactuan todos los NormalItems
    def updateQuality(self):
        if self.getSell_in() > 0:
            self.computeQuality(-2)
        else:
            self.computeQuality(-4)

        self.setSell_in()


class AgedBrie(NormalItem, Interfaz):
    # AgedBrie, hereda el comportamiento y los metodos de NormalItem, Item e Interfaz
    # Por eso, este __init__, ejecuta NormalItem__init__, que a su vez, ejecuta Item__Init__
    # Lo mismo pasará con los demás items
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # El Queso, si no está caducado, suma 1 a su calidad,
    # Si está caducado, suma dos
    def updateQuality(self):
        if self.getSell_in() >= 0:
            self.computeQuality(1)
        else:
            self.computeQuality(2)
        self.setSell_in()


class Backstage(NormalItem, Interfaz):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # El Backstage , como el Brie, incrementa su valor a medida que se caduca
    # Si tiene más de 10 días +1 calidad, +5 días +2 calida, +0 días +3 calidad
    # Si se caduca, 0 calidad
    def updateQuality(self):
        if self.getSell_in() > 10:
            self.computeQuality(1)
        elif self.getSell_in() > 5:
            self.computeQuality(2)
        elif self.getSell_in() >= 0:
            self.computeQuality(3)
        else:
            self.setQuality(0)

        self.setSell_in()


class Sulfuras(NormalItem, Interfaz):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Sulfuras... Ni caduca ni se vende, es legendario
    def updateQuality(self):
        pass


class Conjured(NormalItem, Interfaz):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Este es el nuevo Item, Conjured.
    # Se degrada en calidad, el doble de rapido que los items normales
    # Tan solo hay que mirar más arriba, como se actualizan los items normales

    def updateQuality(self):
        if self.getSell_in() >= 0:
            self.computeQuality(-2)
        else:
            self.computeQuality(-4)

        self.setSell_in()
