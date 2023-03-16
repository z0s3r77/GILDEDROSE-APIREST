from domain.items.Interface import Interfaz
from domain.items.NormalItem import NormalItem


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
