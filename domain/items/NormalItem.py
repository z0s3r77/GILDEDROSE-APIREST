from domain.items.Item import Item


class NormalItem(Item):
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
