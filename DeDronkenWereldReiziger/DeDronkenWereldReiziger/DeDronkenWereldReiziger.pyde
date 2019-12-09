import StartScreen,CreateUsers, RandomStartPositions,QuestionScreen,AnswerScreen,RadScreen, functions
import traceback
screens=[]
goBack=False
gameData={}
def setup():
    global screens
    size(1000,800)
    screens=[StartScreen,CreateUsers, RandomStartPositions,QuestionScreen,AnswerScreen,RadScreen]
index=0
pageSetup=False

def draw():
    global index,pageSetup,screens,goBack,gameData
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
                if index>5:
                    index=3
                    screens[index].shown=True
                    screens[index].eventAllowed=True
                    print('index higher then 5 is out of range so go to next question')
                else:
                    index+=1
                print('goto next screen',index) 
            else:
                if not pageSetup:
                    print('screen',index)  
                    cursor(ARROW)
                    screens[index].setup()
                    if index==1:
                        if screens[index].gameData!=None:
                            gameData=screens[index].gameData
                        print("test")
                        #get the users from createusers and pass them through to randomstartpos
                    if index ==2:
                        screens[index].spelers=gameData['users']
                        
                    pageSetup=True
                
                # if (index==5 ):
                #     if not gameData['alcoholicCheck']:
                #         screens[5].shown=False
                #         screens[5].eventAllowed=False        
                #         index=3
                #     print('Alcohol isnt allowed so dont go to the drink rad')   
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
                i.mouseClicked()
        except Exception as e:
            print('mousepressed caused error in: '+str(i)+' --- ignored\n'+str(e))
            traceback.print_exc()
            
def mouseClicked():
    global screens
    for i in screens:
        try:
            if i.eventAllowed:
                i.mouseClicked()
        except Exception as e:
            print('mouseClicked caused error in: '+str(i)+' --- ignored\n'+str(e))
            traceback.print_exc()

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
        except Exception, e:
            print('mousereleased caused error in: '+str(i)+' --- ignored'+str(e))
            traceback.print_exc()
            
            
def keyPressed():
    global index,screens,goBack,gameData
    if key==TAB and index>0:
        goBack=True
    for i in screens:
        try:
            
            if i.eventAllowed:
                if index==4 and not gameData['alcoholicCheck']:
                    print('Alcohol isnt allowed so dont go to the drink rad')
                    screens[index].shown=False
                    screens[index].eventAllowed=False
                    index=3
                    screens[index].shown=True
                else:
                    i.keyPressed()
        except Exception as e:
            print('keyPressed caused error in: '+str(i)+' --- ignored\n'+str(e))    
            traceback.print_exc()
