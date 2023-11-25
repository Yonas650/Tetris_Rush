import os, random

path = os.getcwd() # get the current working directory of the folder this file is stored in
NUM_ROWS = 20
NUM_COLS = 10
RESOLUTIONX = 200
RESOLUTIONY = 400
BLOCK_WIDTH = RESOLUTIONX/NUM_COLS
BLOCK_HEIGHT = RESOLUTIONY/NUM_ROWS
class Blocks: #creates the Blocks class
    def __init__(self):
        self.r=0
        self.c=self.shuffle()
        self.x=self.c*BLOCK_WIDTH
        self.y=self.r*BLOCK_HEIGHT
        self.w=BLOCK_WIDTH
        self.h=BLOCK_HEIGHT
        self.vy=1
        self.key_handler = {LEFT:False, RIGHT:False, UP:False}
        self.fallen=False
        self.colo=[]
        self.pickcolor()
    def shuffle(self): # each time shuffles the column the blocks fall from
         arr=[]
         for c in range(NUM_COLS+1):
            arr.append(c)
         return random.randint(arr[0],arr[NUM_COLS])
    def gravity(self): # make the bocks fall down
        if self.y<380 and not self.fallen:
            self.y=self.y+20
            
        
    def update(self): #sets the conditions for the right and left key events and detects them   
        if self.key_handler[LEFT] == True and not self.fallen and self.x>=20 and board.lch() :
            self.vx = -20
        elif self.key_handler[RIGHT] == True and not self.fallen and self.x<180 and board.rch():
            self.vx = 20
        else:
            self.vx = 0
        self.x = self.x + self.vx
        
    def pickcolor(self): #random color choice
        redd=[255,51,52]
        blu=[0,0,255]
        gree=[30,183,66]
        yellow=[246,187,0]
        purple=[76,0,153]
        white=[255,255,255]
        black=[0,0,0]
        self.colo=[redd,blu,gree,yellow,purple,white,black]
        self.a=random.choice(self.colo)
          
            
    def display(self): #displays the blocks
        self.update()
        fill(self.a[0],self.a[1],self.a[2])
        rect(self.x,self.y,self.w,self.h)
        self.gravity()
        self.shuffle()
    
    def get_color(self):# returns the color of each block that i use it later to compare blocks in a column
        return self.a
        
        
        
class Board:# this the game class
    def __init__(self, w, h):
        
        self.w = w
        self.h = h
        self.r = NUM_ROWS
        self.c = NUM_COLS
        self.speed=0
        self.blocks = []
        self.blocks.append(Blocks())
        self.xy=[]
        self.counter=0
        self.gameover=0
        
    
    def display(self): #displays the whole game
        a=self.w
        for c in range(self.c,-1,-1):#draws the vertical lines of the board
            line(self.w,0,self.w,self.h)
            self.w-=RESOLUTIONX/NUM_COLS
        self.w=a #reset the value of the width
        b=self.h
        for r in range(self.r,-1,-1):#draws the horizontal lines of the board
            line(0,self.h,self.w,self.h) 
            self.h-=RESOLUTIONY/NUM_ROWS
        self.h=b# resets the value of the height
        
        
        for i in range(len(self.blocks)-1,-1,-1): #displays the blocks in the board
            self.blocks[i].display()
        if self.gameover==False: #makes the game continue as long as the board desn't fill   
            self.checker()
            
        
        
        
        self.chegameover()
        self.wincheck()
        # if self.gameover==True:
        #     self.blocks = [Blocks()]
        
    def checker(self):
        if self.blocks[-1].y == 380 or self.chhh():
            self.blocks[-1].fallen = True
            self.blocks.append(Blocks())
            for b in range(len(self.blocks)):
                if (self.blocks[-1].y + 20) == self.blocks[b].y and self.blocks[-1].x == self.blocks[b].x:
                    self.blocks[-1].fallen = True
            self.speed += 0.25
            self.column_check()
        
    def chhh(self):#checks if there is a block below the falling block
        for b in range(len(self.blocks)):
            if (self.blocks[-1].y+20)== self.blocks[b].y and self.blocks[-1].x== self.blocks[b].x:
                return True
        return False
    def lch(self):#checks if there is a block to the left of the falling block
        for b in board.blocks:
            if self.blocks[-1].x-20==b.x and self.blocks[-1].y+20== b.y:
                return False
        return True
    def rch(self):#checks if there is a block to the right of the falling block
        for b in board.blocks:
            if self.blocks[-1].x+20==b.x and self.blocks[-1].y+20== b.y:
                return False
        return True
    def column_check(self):
        for j in range(0, 200, 20):
            blocksc = []
            for i in range(380, 0, -20):
                for a in range(len(self.blocks)):
                    if self.blocks[a].x == j and self.blocks[a].y == i:
                        blocksc.append(self.blocks[a])

            for a in range(len(blocksc) - 3):
                if (blocksc[a].y == blocksc[a+1].y + 20 == blocksc[a+2].y + 40 == blocksc[a+3].y + 60) and \
                        (blocksc[a].get_color() == blocksc[a+1].get_color() == blocksc[a+2].get_color() == blocksc[a+3].get_color()):
                    self.blocks.remove(blocksc[a])
                    self.blocks.remove(blocksc[a+1])
                    self.blocks.remove(blocksc[a+2])
                    self.blocks.remove(blocksc[a+3])
                    self.counter += 1
                    self.speed = 0
                    
                             
    def gam(self): #prints the Gameover text and the score when the game ends
        if self.gameover==True:
            fill(255,255,255)
            textSize(15)
            text('Gameover'+'\nScore:'+str(self.counter),board.w//2, board.h//2)
    def chegameover(self):#ends the game when the board fills
        if len(self.blocks)==400:
            self.gameover=True
    def wincheck(self):#prints the score
        if self.gameover==False:
            o=self.counter
            fill(0,0,0)
            textSize(15)
            text('Score:'+str(o),130,20)

              
        
    
                   
                
    
            
            
        
    
        
        
board = Board(RESOLUTIONX,RESOLUTIONY)#the board is instantiated 


def setup():
    size(board.w, board.h)
    background(210,210,210)


def draw():
    if frameCount%(max(1, int(8 - board.speed)))==0 or frameCount==1: 
        background(210,210,210)
        board.display()
        board.gam()
        board.wincheck()
def mouseClicked():#detects mouse movements
    global board
    if board.gameover:
         board = Board(RESOLUTIONX,RESOLUTIONY)
        
   
         
        
def keyPressed():#detects the pressing of the left and right keys
    if keyCode == LEFT and board.lch() :
        board.blocks[len(board.blocks)-1].key_handler[LEFT] = True
    elif keyCode == RIGHT and board.rch():
        board.blocks[len(board.blocks)-1].key_handler[RIGHT] = True
        
def keyReleased():#detects the releasing of the left and the right keys
    if keyCode == LEFT:
        board.blocks[len(board.blocks)-1].key_handler[LEFT] = False
    elif keyCode == RIGHT:
        board.blocks[len(board.blocks)-1].key_handler[RIGHT] = False

   
    
    


    
    
