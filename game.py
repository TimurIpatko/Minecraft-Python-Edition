# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from hero import Hero
from mapmanager import Mapmaneger


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmaneger()
        x,y = self.land.loadLand('land2.txt')
        self.hero = Hero((x//2,y//2,2),self.land)
        base.camLens.setFov(90)

game = Game()
game.run()