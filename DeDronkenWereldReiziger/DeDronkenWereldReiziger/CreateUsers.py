#Sander Moerman, INF1K, 0988465
import functions

imageChecked = None
imageNotChecked = None

defaultColor = color(37, 107, 133)

gameData = {}
gameData['alcoholicCheck'] = False
gameData['amountOfUsers'] = False
gameData['errorMessage'] = False
gameData['errorMessage2'] = False
gameData['yPlayer'] = [False, False, False, False]
gameData['users'] = ['', '', '', '']
gameData['blink'] = [False, False, False, False]

colorsToChoose = [color(255, 0, 0), color(0, 255, 0),color(0, 0, 255),color(255, 255, 0)]

screens = {}
screens['secondScreen'] = False

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

    text("Welkom bij ons digitale component \n Met hoeveel spelers wilt u spelen? \n kies uit 2, 3 of 4 spelers", width / 2, 300)

    # a rectangle where the user input is shown
    functions.createRectWithColor(width/2 - 200, 400, 400, 50, defaultColor)
    
    # a rectangle where the user can check if the alchol is allowed or not
    functions.createRectWithColor(660, 680, 50, 50, defaultColor)
    
    # showing the default image which is not checked
    imageMode(CENTER)
    image(imageNotChecked, width / 1.46, height / 1.13, 65, 65)
    
    fill(255)
    text('Klik het vakje aan om de drank\n variant te spelen', width/2.1, 700)
    
    # if alcoholicCheck is true the box will be checked
    if(gameData['alcoholicCheck']):
        imageMode(CENTER)
        image(imageChecked, width / 1.46, height / 1.13, 65, 65)
        
    functions.blink(defaultValueBlink, 410, defaultValueBlink, 440)
    
    if(gameData['amountOfUsers'] != 0):
        text(gameData['amountOfUsers'], width/2, 430)
   
    if(gameData['errorMessage'] != False):     
        text(gameData['errorMessage'], width/2, 500)
        
    if(screens['secondScreen']):
        functions.clearPage()
        
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
                functions.showImage(imageChecked, 760+(60/2), 200+(50/2)+(i*150))
            else:
                functions.showImage(imageNotChecked, 761+(60/2), 200+(50/2)+(i*150))
                
def mouseClicked():
    global gameData, defaultValueBlink
    
    alcoholicVariant = functions.onRect(660, 680, 50, 50)
        
    if(alcoholicVariant):
        gameData['alcoholicCheck'] = not gameData['alcoholicCheck']
        
    for i in range(len(gameData['blink'])):
        if functions.onRect(300, 200 + (150 * i), 400, 50,) and screens['secondScreen']:
            gameData['blink'][i] = True
            
            functions.clearUserInput()
            
            if(len(gameData['users'][i]) == 0):
                defaultValueBlink = 500
            else:
                defaultValueBlink = functions.loopThroughBlink(gameData['users'][i])
            
        else:
            gameData['blink'][i]= False   
            
    for i in range(len(gameData['yPlayer'])):
        if functions.onRect(760,  200+(i*150), imgWidth,imgHeight) and screens['secondScreen']:
            
            if(gameData['users'][i] == ''):
                gameData['errorMessage2'] = 'Naam mag niet leeg zijn'
                gameData['yPlayer'][i]= False
            else:
                gameData['errorMessage2'] = False
                gameData['yPlayer'][i]= True
        else:
            gameData['yPlayer'][i]= False
            
def keyPressed():
    global gameData, defaultValueBlink, shown
    
    users = 0
    
    if(key != ENTER and screens['secondScreen'] == False):
        
        gameData['amountOfUsers'] = functions.amountOfUsers()
        defaultValueBlink = functions.PositionBlink(gameData['amountOfUsers'], 1)
        
        if(gameData['amountOfUsers'] == 0):
            gameData['errorMessage'] = 'Dit is geen 2, 3 of 4'
        else:
            gameData['errorMessage'] = False
            
    if(key == ENTER and gameData['amountOfUsers'] == False):
        gameData['errorMessage'] = 'Vul iets in voordat u doorgaat naar de volgende pagina' 
    else:
        if(key == ENTER and gameData['errorMessage'] == False):
            screens['secondScreen'] = True
            
    for i in range(len(gameData['blink'])):
        if gameData['blink'][i]:
            if(len(gameData['users'][i]) >= 0):
                defaultValueBlink = functions.pushBlink(gameData['users'][i])
                gameData['users'][i] = functions.createUser(gameData['users'][i])

        if(len(gameData['users'][i]) >= 1):
            users += 1
            gameData['errorMessage2'] = False
            
    if(key == ENTER and screens['secondScreen']):    
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
        
                        if(int(gameData['amountOfUsers']) == users):
                            screens['thirdScreen'] = True
                            shown = False
