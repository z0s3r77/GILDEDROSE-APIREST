from domain.items.NormalItem import NormalItem


class Conjured(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Este es el nuevo Item, Conjured.
    # Se degrada en calidad, el doble de rapido que los domain normales
    # Tan solo hay que mirar más arriba, como se actualizan los domain normales

    def updateQuality(self):
        if self.getSell_in() >= 0:
            self.computeQuality(-2)
        else:
            self.computeQuality(-4)

        self.setSell_in()
