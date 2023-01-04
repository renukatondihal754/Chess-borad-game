from coin import Coin
class Horse(Coin):
    offset=[(1,2),(-1,2),(-2,1),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]  #stactik varibale

    def __init__(self,x,y):
        super().__init__(x,y)
        self.repr="H" # repr represtion

    def genMoves(self): # generte moves
        cx,cy=self.pos
        return [(cx+ox,cy+oy) for ox,oy in Horse.offset]  # list compresion # cx(current x postion)

    def __repr__(self):
        return self.repr

h=Horse(1,2)
print(h.genMoves())


