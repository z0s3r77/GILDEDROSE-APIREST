from domain.items.NormalItem import NormalItem


class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Sulfuras... Ni caduca ni se vende, es legendario
    def updateQuality(self):
        pass
