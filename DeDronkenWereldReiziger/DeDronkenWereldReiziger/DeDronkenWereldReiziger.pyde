import StartScreen,CreateUsers, RandomStartPositions,QuestionScreen,AnswerScreen,RadScreen
screens=[]
goBack=False
def setup():
    global screens
    size(1000,800)
    screens=[StartScreen,CreateUsers, RandomStartPositions,QuestionScreen,AnswerScreen,RadScreen]
index=0
pageSetup=False

def draw():
    global index,pageSetup,screens,goBack
    if goBack:
        screens[index].shown=True
        screens[index].eventAllowed=False
        index-=1
        screens[index].shown=True
        screens[index].eventAllowed=True
        print("going back")
        goBack=False
    if screens!=None:
        try:
            if not screens[index].shown:
                pageSetup=False
                index+=1
                print('goto next screen',index) 
            else:
                if not pageSetup:
                    print('screen',index)  
                    cursor(ARROW)
                    screens[index].setup()
                    pageSetup=True
                screens[index].draw()
        except Exception, e:
            #exception was thrown go back to last page
            if(index>0):
                index-=1
                screens[index].shown=True
            else:
                index=0
                screens[index].shown=True
            print(str(e))
   
def mousePressed():
    global screens
    for i in screens:
        try:
            if i.eventAllowed:
                i.mousePressed()
                i.mouseClicked()
        except Exception, e:
            print('error by mousepressed in: '+str(i)+' --- ignored\n'+str(e))

# def mouseClicked():
#     global screens
#     for i in screens:
#         try:
#             if i.eventAllowed:
#                 i.mouseClicked()
#         except Exception, e:
#             print('error by mouseClicked in: '+str(i)+' --- ignored\n'+str(e))

def mouseReleased():
    global screens
    for i in screens:
        try:
            if i.eventAllowed:
                i.mouseReleased()
        except:
            print('error by mousereleased in: '+str(i)+' --- ignored')
def keyPressed():
    global index,screens,goBack
    if key==TAB and index>0:
        goBack=True
    for i in screens:
        try:
            if i.eventAllowed:
                i.keyPressed()
        except:
            print('error by keyPressed in: '+str(i)+' --- ignored')    
