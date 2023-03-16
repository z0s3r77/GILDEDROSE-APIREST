from domain.items.Interface import Interfaz
from domain.items.NormalItem import NormalItem


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
