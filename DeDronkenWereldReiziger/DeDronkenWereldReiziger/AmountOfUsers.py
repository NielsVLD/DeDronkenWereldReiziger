#Sander Moerman, INF1K, 0988465
import functions

imageChecked = None
imageNotChecked = None

defaultColor = color(37, 107, 133)

gameData = {}
gameData['alcoholicCheck'] = False
gameData['amountOfUsers'] = False
gameData['errorMessage'] = False

# array where all the sended data is included
sendJsonData = []

defaultValueBlink = 500

imgWidth=60
imgHeight=50

shown = True

def setup():   
    global imageChecked, imageNotChecked
    
    fill(37, 107, 133)
    # size of the project
    size(1000, 800)

    # color and thickness of the lines
    stroke(255, 188, 0)
    strokeWeight(2)
    
    imageChecked = loadImage('images/checked.png')
    imageNotChecked = loadImage('images/notchecked.png')
    
def draw():
    background(51)
    
    textAlign(CENTER)

    # text size and color for the rest of this project
    textSize(20)
    fill(255)

    text("Welkom bij De Dronken Wereld Reiziger \n Met hoeveel spelers wilt u spelen? \n kies uit 2, 3 of 4 spelers", width / 2, 300)

    # a rectangle where the user input is shown
    functions.createRectWithColor(width/2 - 200, 400, 400, 50, defaultColor)
    
    # a rectangle where the user can check if the alchol is allowed or not
    functions.createRectWithColor(660, 620, 50, 50, defaultColor)
    
    functions.createRectWithColor(width/2 - 100, 700, 200, 50, defaultColor)
    fill(255)
    text('Volgende', width/2, 730)
    
    # showing the default image which is not checked
    functions.showImage(imageNotChecked, width / 1.46, height / 1.22)
    
    fill(255)
    text('Klik het vakje aan om de drank\n variant te spelen', width/2.1, height/ 1.24)
    
    # if alcoholicCheck is true the box will be checked
    if(gameData['alcoholicCheck']):
        functions.showImage(imageChecked, width / 1.46, height / 1.22)
        
    functions.blink(defaultValueBlink, 410, defaultValueBlink, 440)
    
    if(gameData['amountOfUsers'] != 0):
        text(gameData['amountOfUsers'], width/2, 430)
   
    if(gameData['errorMessage'] != False):     
        text(gameData['errorMessage'], width/2, 500)
                
def mousePressed():
    global gameData, defaultValueBlink, shown, sendJsonData
            
    if(functions.onRect(660, 620, 50, 50)):
        gameData['alcoholicCheck'] = not gameData['alcoholicCheck']
   
    if(functions.onRect(width/2 - 100, 700, 200, 50) and gameData['amountOfUsers'] != False):
        
        sendJsonData.append({
            'amountOfUsers': gameData['amountOfUsers'],
            'alcoholicCheck': gameData['alcoholicCheck']
        })
        
        functions.dumpJson('gameData.json', sendJsonData)
        
        # when the amountOfUsers is correct this page will be showned false
        shown = False
        
def keyPressed():
    global gameData, defaultValueBlink, shown
    
    if(key != ENTER):
        
        gameData['amountOfUsers'] = functions.amountOfUsers()
        defaultValueBlink = functions.PositionBlink(gameData['amountOfUsers'], 1)
        
        if(gameData['amountOfUsers'] == 0):
            gameData['errorMessage'] = 'Dit is geen 2, 3 of 4'
        else:
            gameData['errorMessage'] = False
            
    if(key == ENTER and gameData['amountOfUsers'] == False):
        gameData['errorMessage'] = 'Vul iets in voordat u doorgaat naar de volgende pagina'      
    else:
        if(key == ENTER and gameData['amountOfUsers'] != False):
            shown = False
