import json

# -----------------------------------------        
# for the json crud
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/    
# -----------------------------------------        

gameData = {}
userNames = []
test = None
counter = 0

def getJson():
    with open('gameData.txt') as json_file:
        gameData = json.load(json_file)
        
    return gameData

def clearPage():
    background(0)
    background(51)
    
def createUsers():
    global test, gameData, counter

    gameData = getJson()
    
    i = 1

    text('Vul hieronder in uw naam speler ' + str(i), width/2, 20)
    textAlign(CENTER)
    
    rect(width/4, height/ 5, 300, 80)
    fill(37, 107,133)
    
def onRect(x, y, width, height):
    return(mouseX >= x and mouseX <= x + width and mouseY >= y and mouseY <= y + height)



    
