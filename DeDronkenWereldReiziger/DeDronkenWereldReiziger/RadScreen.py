# Reindert
# 0990526

# Voor navigatie
shown=True
answeredCorrect=False
rotation = 2.0
rotating=False
speed=random(0.1,1.9)
# list of actions
drinkActions=["1 shot","2 shots","iedereen 1 shot","1 atje","iedereen atten","2 shotjes","4 slokken","1 atje","1 slok","2 atjes","2 shots","3 slokken","8 slokken","5 slokken"]
radHeight=600
allowedToLeaveScreen=False

def setup():
    size(1000,800)
    print("now on radScreen")
    
def draw():
    global rotation,rotating,speed,radHeight,answeredCorrect,allowedToLeaveScreen
    
    background(51)
    textSize(25)
    textAlign(CENTER,CENTER)
    
    
    #show hand cursor when hovering over buttons and rad
    if overCircle(width/2,height/2,radHeight) or isMouseWithinRect((width)-175,height-100,150,50):
        cursor(HAND)
        fill(255,188,0)
    else:
        cursor(ARROW)
        fill(255)
    text("Klik op het rad om te draaien!",width/2,60)
    fill(255)
    if answeredCorrect:
        textAlign(CENTER,CENTER)
        text("De vraag was goed beantwoord: Deel uit!",width/2,25)
    else:
        textAlign(CENTER,CENTER)
        text("De vraag was fout beantwoord: Drink zelf!",width/2,25)
    push()
    translate(width/2, height/2)
    drawLegs()
    #rotates the canvas 
    rotate(PI*rotation)
    drawRad(0,0,radHeight)
    fill(51)
    # % per item
    piecePercentage= 100.0/(len(drinkActions)*2)
    # old % + the new item %
    oldPiecePercentage=0.0
    
    # the text now scales on the bases of the amount of items
    circumference=PI*radHeight
    heightOfOneItem = circumference/len(drinkActions)
    # text is a sixth of the height of one item
    txtSize = heightOfOneItem/6
    stroke(255,188,0)
    textSize(txtSize if txtSize<17 else 17)
    
    i=0
    while i< len(drinkActions)*2:
        # 2 /100 cause 2*pi=360 deg
        lineAngle=(((2.0 / 100.0) * (oldPiecePercentage + piecePercentage)) * PI)
        rLine = xyOnArc(0, 0, radHeight/2, lineAngle)
        rTxt= xyOnArc(0, 0, (radHeight/4), lineAngle)
        oldPiecePercentage+=piecePercentage
        
        if i%2!=0:
            line(0,0,rLine[0],rLine[1])
        else:
            fill(255,188,0)
            push()
            translate(rTxt[0],rTxt[1])
            rotate(lineAngle)
            if i==1:
                print(degrees(lineAngle))
            
            
            textAlign(CENTER,CENTER)
            text(drinkActions[i/2],0,0)
            pop()
        
        i+=1
        
    drawRad(0,0,50)
    pop()
    drawArrow()
    rotationHandler()
    allowedToLeaveScreen=True
    stroke(255,188,0)
    strokeWeight(2)
    fill(37, 107,133)
    rect((width)-175,height-100,150,50)
    fill(255)
    textAlign(CENTER,CENTER)
    text("Volgende",(width-100),height-75,)


    
def rotationHandler():
    global rotating,rotation,speed
    if rotating:
        if rotation>0.0:
            rotation-=speed
        else:
            rotation=2.0
        if speed>0:
            print(speed)
            speed-=0.01
        else:
            rotating=False
            speed=random(0.3,1.9)
            

# drawing ui        
def drawRad(x,y,s):
    fill(37, 107,133)
    stroke(255,188,0)
    strokeWeight(2)
    circle(x,y,s)
    
def drawArrow():
    triStartP= [0,0]
    triP2 =[-20,75]
    triP3=[20,75]
    if rotating:
        fill(255)
        stroke(255)
    else:
        fill(0,255,0)
        stroke(0,255,0)
    push()
    translate((width/2), (height/2)+((radHeight/2)-50))
    triangle(triStartP[0],triStartP[1],triP2[0],triP2[1],triP3[0],triP3[1])
    triangle(triStartP[0],triStartP[1]+100,triP2[0],triP2[1],triP3[0],triP3[1])
    pop()
    fill(255)
    stroke(255)
    
def drawLegs():
    fill(110,80,64)
    stroke(255,188,0)
    strokeWeight(0)
    triangle(0,0,150,(height/2)-25,250,(height/2)-25)
    triangle(0,0,-150,(height/2)-25,-250,(height/2)-25)
        
# events    
def mouseReleased():
    global rotating,radHeight
    if overCircle(width/2,height/2,radHeight) and not rotating:
        print("rotate rad")
        rotating=not rotating    
    
def mousePressed():
    global shown, allowedToLeaveScreen
    if isMouseWithinRect((width)-175,height-100,150,50) and allowedToLeaveScreen:
        # nextPage
        shown=False
def isMouseWithinRect(x,y,w,h):
    return (x < mouseX < x + w and y < mouseY < y + h)            
def keyPressed():
    global rotating, shown,thisScreenIsBeingDrawn
    if key==ENTER:
        shown=False
        thisScreenIsBeingDrawn=False
    if key == TAB and not rotating:
        rotating=not rotating
        
# maths        
def overCircle(x, y, diameter) :
    disX = x - mouseX
    disY = y - mouseY
    return (sqrt(sq(disX) + sq(disY)) < diameter/2 )

def xyOnArc(cx, cy, rad, radiusAng):
    # center to end of radius in x direction times the cosines of the radius gets the x coord
    x = cx + rad * cos(radiusAng)
    # center to end of radius in y direction times the sines of the radius gets the y coord
    y = cy + rad * sin(radiusAng)
    return [x, y];
