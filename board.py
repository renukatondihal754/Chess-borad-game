from horse import Horse
class Board:
    def __init__(self,rows=8,cols=8):
        self.rows=rows
        self.cols=cols
        self._initGrid()   # only private purpose use it means acces inside only

    def _initGrid(self):
        grid=[]     
        for i in range(self.rows):
            row=[]
            for j in range(self.cols):
                row.append('_')
            grid.append(row)
        self.grid=grid


    def __str__(self): #string represtion of borad 
        s=''
        for row in self.grid:
    
            for col in row:
                s+=f' {col} '
            s+="\n"
        return s 

    def putHorse(self,h):
        self.horse=h
        self.grid[h.pos[0]][h.pos[1]]=h  #0,1 are the tuples were horse kept this value goes to coin.py, self.pos=(x,y)

    
    def updateBoard(self):
        moves=self.horse.genMoves()

        for move in moves:
            if self.valid(move):
                x,y=move
                self.grid[x][y]='x' #'x' is next move of horse

    def valid(self,move):
        x,y=move
        if x>=self.rows or x<0 or y>=self.cols or y<0:
            return False
        return True
    
    
if __name__ =='__main__':
   b=Board()
   b.putHorse(Horse(3,3))
   print(b)
   b.updateBoard()
   print(b)
    
