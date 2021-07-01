from os import *
from random import *
from time import *
from math import *

class Pivot():
    def __init__(self ,x = 0, y=0 ):
        self.x = x
        self.y = y 
        self.mass = uniform(1 , 1.5)
        self.speed = [0,0] # [x, y]
        self.display = "s"
        self.time= 0
    def draw(self, matrix):
        matrix[round(self.y)][round(self.x)] = self.display
        return matrix
class Cube(Pivot):
    def __init__(self ,x = 0, y=0 ):
        Pivot.__init__(self ,x ,y )
        self.mass = 9
    def draw(self, matrix):
        for i in [[0, 1], [1,1], [-1,1], [0,2], [0,0]]:
            matrix[round(self.y + i[1] -2)][round(self.x + i[0])] = self.display
        return matrix
    
        

class world():
    def __init__(self , size = [20, 20]):# size[x, y]
        self.size = size
        self.main = []
        self.gravity = 0.001
        self.time = 0
        self.back = " "
        self.wait = 0.001
        
        self.view = self.ClearView(size[0], size[1])
    
    def ClearView(self, x ,y , back = "0"):
        View = list()
        for i in range(0,y +10 ):
            View.append([])
            for i2 in range(0, x +10):

                View[i].append(self.back)
                if i >= y +1 :
                    View[i][i2] = "="             

                #print(View)
        self.view = View
        return View 

    def View(self):
        self.ClearView(self.size[0], self.size[1])        
        

        for i in self.main:
            self.view = i.draw(self.view) 
        system('cls||clear')
        for y in self.view:
            for x in y:
                print(x, end=" ")
            print()
        print("Time: {}".format(self.time) )


    def physics(self):
        for i in self.main:
            
            #print(i.speed)
            #!!!logic physics!!!
            #print(i.speed)
            if i.y >= self.size[1]:
                i.speed[1] = i.speed[1] *-1
                if i.y >= self.size[1]:
                    i.y = self.size[1]
                

            
            
            
            if i.speed[1] >= 0: 
                i.speed[1] = i.speed[1] + self.gravity *i.time * i.mass
                
            else : 
                i.speed[1] = i.speed[1] + self.gravity * i.time * i.mass
                #print(i.speed)
                #print(self.gravity * i.time * i.mass)
                #sleep(10)
            
        for i in self.main:
            i.x += i.speed[0]
            i.y += i.speed[1]
            i.time +=1
            #print(i.x, i.y)
        self.time +=1 
    

    
    def Main(self, end , wait = None ):
        if wait == None:
            wait = self.wait
        for x in range(0, end):
            try:                    
                self.physics()
                self.View()
                sleep(wait)
            except IndexError:
                
                print("ouupssss")
                self.Main(x)


if __name__ == '__main__':
    input("start?")
    try:
        World = world([70,  50])
        for x in range(0, 20):
            World.main.append(Pivot(x=randint(0, 30)))

        World.main.append(Cube(x = 10, y = 10))
        World.Main(9999999)
    except KeyboardInterrupt:
        print("error")
        input()    
        