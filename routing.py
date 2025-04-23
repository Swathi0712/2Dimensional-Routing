import random
import turtle

def generateGrid(rows, cols):
    #Create a 2D array
    grid = [[0]*rows]*cols
    #initialising the matrix
    print(grid)

    #Generate a random integer matrix
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            grid[i][j] = random.randint(1,100)
    print(grid)

    return grid


#Method to create and visualize grid
def drawGrid(rows, cols, cellSize):

    for col in range(cols):
        x = col * cellSize
        trtle.goto(x,0)
        trtle.pendown()
        trtle.goto(x,(cols-1)*cellSize)
        trtle.penup()

    for row in range(rows):
        y = row * cellSize
        trtle.goto(0,y)
        trtle.pendown()
        trtle.goto((rows-1)*cellSize,y)
        trtle.penup()

sc = turtle.Screen()
trtle = turtle.Turtle()

# set screen
sc.setup(800,800)    
 
# set turtle features
trtle.speed(10)
trtle.color('blue')
trtle.penup()

gr = generateGrid(8,8)
dr = drawGrid(8,8, 40)

turtle.Screen().exitonclick() 













