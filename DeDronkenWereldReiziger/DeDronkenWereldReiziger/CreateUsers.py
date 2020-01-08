#Sander Moerman, INF1K, 0988465
import functions

imageChecked = None
imageNotChecked = None

defaultColor = color(37, 107, 133)

gameData = {}
# gameData['alcoholicCheck'] = False
# gameData['amountOfUsers'] = False
# gameData['errorMessage'] = False
gameData['errorMessage2'] = False
gameData['yPlayer'] = [False, False, False, False]
gameData['users'] = ['', '', '', '']
gameData['blink'] = [False, False, False, False]

colorsToChoose = [color(255, 0, 0), color(0, 255, 0),color(0, 0, 255),color(255, 255, 0)]

defaultValueBlink = 500

imgWidth=60
imgHeight=50

shown = True

jsonData = []

goToStartPositionScreen = False

def setup():   
    global imageChecked, imageNotChecked, jsonData
    
    fill(37, 107, 133)
    # size of the project
    size(1000, 800)

    # color and thickness of the lines
    stroke(255, 188, 0)
    strokeWeight(2)
    
    imageChecked = loadImage('images/checked.png')
    imageNotChecked = loadImage('images/notchecked.png')
    
    jsonData = functions.getJson('gameData.json')
    
def draw():
    background(51)
    
    textAlign(CENTER)

    # text size and color for the rest of this project
    textSize(20)
    fill(255)
        
    
    
    text('Kleur', 200, 125)
    text('Naam', width/2, 125)
    text('Jongste speler', 790, 125)
    
    if(gameData['errorMessage2'] != False):     
        text(gameData['errorMessage2'], width/2, 170)
    
    for i in range(4):
        functions.createRectWithColor(300, 200 + (150 * i), 400, 50, defaultColor)
        if(gameData['blink'][i] != False):
            functions.blink(defaultValueBlink, 210 + (150* i), defaultValueBlink, 240 + (150 * i))
        
        text(str(gameData['users'][i]), width/2, 230+(i*150))
        functions.createRectWithColor(180, 200+(i*150), 50, 50, colorsToChoose[i])
        if gameData['yPlayer'][i]:
            functions.showImage(imageChecked, 760+(imgWidth/2), 200+(imgHeight/2)+(i*150))
        else:
            functions.showImage(imageNotChecked, 761+(imgWidth/2), 200+(imgHeight/2)+(i*150))
            
    functions.createRectWithColor(width/2 - 100, 725, 200, 50, defaultColor)
    text('Volgende', width/2, 755)
    if functions.onRect(750, 185, 80,80) or functions.onRect(750, 185+(1*150), 80,80) or functions.onRect(750, 185+(2*150), 80,80)or functions.onRect(750, 185+(3*150), 80,80):
        cursor(HAND)
    else:
        cursor(ARROW)
                
def mousePressed():
    
    # screens
    global gameData, defaultValueBlink, shown
    
    
    if(functions.onRect(width/2 - 100, 725, 200, 50)):
        print('test122345')
        keyPressed()
        
        shown = False

    for i in range(len(gameData['blink'])):
        if functions.onRect(300, 200 + (150 * i), 400, 50,):
            gameData['blink'][i] = True
            
            functions.clearUserInput()
            
            if(len(gameData['users'][i]) == 0):
                defaultValueBlink = 500
            else:
                defaultValueBlink = functions.loopThroughBlink(gameData['users'][i])
            
        else:
            gameData['blink'][i]= False   
            
    for i in range(len(gameData['yPlayer'])):
        if functions.onRect(750, 185+(i*150), 80,80):
            print('maak gebruiker aan!')
            if(gameData['users'][i] == ''):
                gameData['errorMessage2'] = 'Naam mag niet leeg zijn'
                gameData['yPlayer'][i]= False
            else:
                gameData['errorMessage2'] = False
                gameData['yPlayer'][i]= True
        else:
            gameData['yPlayer'][i]= False
            
        
       
            
def keyPressed():
    
    # screens
    global gameData, defaultValueBlink, shown
    
    users = 0
    
    
            
    for i in range(len(gameData['blink'])):
        if gameData['blink'][i]:
            if(len(gameData['users'][i]) >= 0):
                defaultValueBlink = functions.pushBlink(gameData['users'][i])
                gameData['users'][i] = functions.createUser(gameData['users'][i])

        if(len(gameData['users'][i]) >= 1):
            users += 1
            gameData['errorMessage2'] = False
            
    if(key == ENTER or goToStartPositionScreen):   
        if(users == 0):
            gameData['errorMessage2'] = 'Vul eerst het formulier in voordat u op verzenden drukt'
        else:
            gameData['errorMessage2'] = False
            
            if(int(gameData['amountOfUsers']) > int(users)):
                gameData['errorMessage2'] = 'U moet meer spelers aanmaken'
            else:
                gameData['errorMessage2'] = False
        
                if(int(gameData['amountOfUsers']) < users):
                    gameData['errorMessage2'] = 'U moet minder spelers aanmaken'
                else:
                    gameData['errorMessage2'] = False
                    
                    if(gameData['yPlayer'][0] == False and gameData['yPlayer'][1] == False and gameData['yPlayer'][2] == False and gameData['yPlayer'][3] == False):
                        gameData['errorMessage2'] = 'kies de jongste speler!'
                    else:
                        gameData['errorMessage2'] = False
                        

                        
                       
                        
                        if(int(jsonData[0]['amountOfUsers']) == users):
                            print('yeah')
                            # shown = False
            
                            
                            
                            
