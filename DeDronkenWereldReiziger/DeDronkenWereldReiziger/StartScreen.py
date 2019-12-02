mapBackground=None
mScale=2
yPos=0
xPos=0
randomPointX=0
randomPointY=0
speed=1
zoomIn=True
title=None
subtitle=None
startClicked=False
def setup():
    global mapBackground,randomPointX,randomPointY,zoomIn,title,subtitle,button
    size(1000,800)
    mapBackground = loadImage("map.png")
    title = loadImage("title.png")
    subtitle = loadImage("subtitle.png")
    button = loadImage("button.png")
    randomPointX = getRandomXPointOnMap()
    randomPointY = getRandomYPointOnMap()
    
    zoomIn= 0>random(0,2)
    
def draw():
    global title,subtitle,button,startClicked
    background(51)
    drawAnimatingMap()
    imageMode(CENTER)
    if title!=None:
        image(title, width/2,50)
    if subtitle!=None:
        image(subtitle, width/2,height/2)
    if button!=None:
        if onRect((width/2)-250,(height-100),500,200):
            cursor(HAND)
            if startClicked:
                image(button, width/2,height-50,500*0.95,85*0.95)
            else:
                image(button, width/2,height-50,500*1.05,85*1.05)
        else:
            cursor(ARROW)
            image(button, width/2,height-50,500,85)
def drawAnimatingMap():
    global mapBackground,mScale,xPos,yPos,randomPointX,randomPointY,speed,zoomIn
    imageMode(CENTER)
    if mapBackground!=None:
        image(mapBackground, (width/2)+xPos, (height/2)+yPos,969*mScale,539*mScale);
    
    if (randomPointX>0 and xPos<randomPointX) and xPos<969:
        xPos+=1*speed
    elif  (randomPointX<0 and xPos>randomPointX)and xPos>-969:
        xPos-=1*speed
    else:
        randomPointX = getRandomXPointOnMap()
        # zoomIn= not zoomIn
        print("zoomin",zoomIn)
    if (randomPointY>0 and yPos<randomPointY)and yPos<539:
        yPos+=1*speed
    elif  (randomPointY<0 and yPos>randomPointY)and yPos>-539:
        yPos-=1*speed
    else:
        randomPointY = getRandomYPointOnMap()
        # zoomIn= not zoomIn
        print("zoomin",zoomIn)
        
def getRandomXPointOnMap():
    x=random(-(400),400)
    print("x",x)
    return x
def getRandomYPointOnMap():
    y=random(-(40),40)
    print("y",y)
    return y
def onRect(x, y, w, h):
    return(mouseX >= x and mouseX <= x + w and mouseY >= y and mouseY <= y + h)
def mousePressed():
    global startClicked
    if onRect((width/2)-250,(height-100),500,200):
        startClicked=True
        
def mouseReleased():
    global startClicked
    if onRect((width/2)-250,(height-100),500,200):
        startClicked=False        
