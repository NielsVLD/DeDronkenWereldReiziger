#Reindert

# Voor navigatie en ontvangen van events als keypressed
shown=True
eventAllowed=False

rotation = 2.0
rotating=False
speed=random(0.1,1.9)
# ,"boe","schaap","test","test1"
drinkActions=["1 shot","2 shots","iedereen 1 shot","1 atje","iedereen atten","2 shotjes","4 slokken","1 atje","1 slok","2 atjes","2 shots","3 slokken","8 slokken","5 slokken"]
radHeight=650

def setup():
    size(1000,800)
    
def draw():
    global rotation,rotating,speed,radHeight
    background(51)
    textSize(25)
    if overCircle(width/2,height/2,radHeight):
        cursor(HAND)
        textAlign(CENTER,CENTER)
        text("Klik om te draaien!",width/2,25)
    else:
        cursor(ARROW)
    push()
    translate(width/2, height/2)
    drawLegs()
    
    rotate(PI*rotation)
    drawRad(0,0,radHeight)
    fill(51)
    # rect(-25, -25, 50, 50)
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
            speed=random(0.1,1.9)
            

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
    stroke(255)
    fill(255)
    push()
    translate((width/2), (height/2)+((radHeight/2)-50))
    triangle(triStartP[0],triStartP[1],triP2[0],triP2[1],triP3[0],triP3[1])
    triangle(triStartP[0],triStartP[1]+100,triP2[0],triP2[1],triP3[0],triP3[1])
    pop()
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
        rotating=not rotating
            
def keyPressed():
    global rotating
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
