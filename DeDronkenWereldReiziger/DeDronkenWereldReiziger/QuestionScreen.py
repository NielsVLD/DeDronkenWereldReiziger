ingevuldAntwoord = False
touched = False
img = None
img1 = None
shown=True
firstTime = True
def setup():
    global img,img1
    size(1000,800)
    img = loadImage('checked.png')
    img1 = loadImage('notchecked.png')

def draw():
    global ingevuldAntwoord,firstTime
    background(51)
    
    fill(37, 107,133)
    # fill(0)
    stroke(255,188,0)
    strokeWeight(2)
    rect(0,0,width,height)

    textAlign(CENTER)
    textSize(20)
    fill(255)
    text("Hawaii behoort ook tot Oceanie",width/2,63)
    text("Vraag:",width/2,30)
    line(0,37, width, 37)
    text("Antwoord:",width/2,120)
    line(0,127, width, 127)
    
    textSize(23)
            
    fill(255)
    text("Waar",width/4,210)
    if not ingevuldAntwoord:
        fill(37, 107,133)
        
    else:
        fill(255)
            
    circle(180, 200, 30)
    imageMode(CENTER)
    if ingevuldAntwoord and not firstTime:
        image(img,180, 200,47.5,40)
    else:
        image(img1,180, 200,40,40)
    fill(255)
    text("Niet waar",width/3.6,260)
    if ingevuldAntwoord:
        fill(37, 107,133)
    else:
        fill(255)   
    circle(180, 250, 30)
    if not  ingevuldAntwoord and not firstTime:
        image(img,180, 250,47.5,40)
    else:
        image(img1,180, 250,40,40)
    fill(37, 107,133)
    rect((width/2)-75,height-100,150,50)
    fill(255)
    textAlign(CENTER,CENTER)
    text("Controleren",(width/2),height-75,)
    
    if isMouseWithinRect(180-15, 200-15,30,30) or isMouseWithinRect(180-15, 250-15,30,30) or isMouseWithinRect((width/2)-75,height-100,150,50):
        cursor(HAND) 
    else:
        cursor(ARROW)
    

def isMouseWithinRect(x,y,w,h):
    
    return (x < mouseX < x + w and y < mouseY < y + h)
 
def mousePressed():
    global ingevuldAntwoord, touched, firstTime, shown
    if isMouseWithinRect(190-20, 200-15,30,30):
        firstTime = False
        ingevuldAntwoord=True
    elif isMouseWithinRect(180-15, 250-15,30,30):
        firstTime = False
        ingevuldAntwoord=False

    
    if isMouseWithinRect((width/2)-75,height-100,150,50):
        # nextPage
        print("to next page ingevuld antwoord: ",ingevuldAntwoord)
        shown=False
