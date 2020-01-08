import StartScreen,AmountOfUsers, CreateUsers, RandomStartPositions,QuestionScreen,AnswerScreen,RadScreen, functions
import traceback
import random as rdm
screens=[]
goBack=False
gameData={}
jsonData={}
qanda={}
currentQuestion={}
currentAnswer='Geen'
questionAnsweredCorrect=False
def setup():
    global screens,qanda
    size(1000,800)
    screens=[StartScreen, AmountOfUsers, CreateUsers, RandomStartPositions,QuestionScreen,AnswerScreen,RadScreen]
    qanda = functions.getJson('qanda.json')
index=0
pageSetup=False
def getRandomQuestion():
    global qanda
    try:
        if len(qanda)==0:
            qanda = functions.getJson('qanda.json')
            qanda.shuffle()
        item =rdm.choice(qanda)
        qanda.remove(item)
        return item
    except Exception, e:
        print("could not get question",e)
        
def SetupPage3():
    global currentQuestion
    currentQuestion= getRandomQuestion()
    #get the first object from the questionobject
    currentQuestion= currentQuestion[currentQuestion.keys()[0]]
    screens[4].vraag=currentQuestion['question']
    print("Random question sent through to screen\n",currentQuestion)
   
def SetupPage4(): 
    global currentQuestion
    screens[5].vraag=screens[4].vraag
    screens[5].punten_goed_antwoord=1
    screens[5].antwoord=currentAnswer
    try:
        screens[5].goede_antwoord=currentQuestion['answers'][str(currentQuestion['answer'])]   
    except Exception, e:
        print('currentQuestion',currentQuestion)
        print("could not get answers",e)    
    
def draw():
    global index,pageSetup,screens,goBack,gameData,currentAnswer,questionAnsweredCorrect,jsonData
    
    if screens!=None:
        try:
            if goBack:
                screens[index].shown=True
                index-=1
                screens[index].shown=True
                print("going back")
                goBack=False
            if not screens[index].shown:
                pageSetup=False
                if index==6:
                    index=4
                    screens[6].shown=True
                    screens[5].shown=True
                    screens[4].shown=True
                else:
                    index+=1
                print('goto next screen',index) 
            else:
                if (index != 6) or (index==6 and jsonData['alcoholicCheck']):
                    
                    if not pageSetup:
                        if jsonData!={}:
                            print("use alcohol",jsonData['alcoholicCheck'])
                        print('screen',index)  
                        cursor(ARROW)
                        screens[index].setup()
                        if index==2:
                            if screens[1].sendJsonData!=None and len(screens[1].sendJsonData)!=0:
                                jsonData=screens[1].sendJsonData[0]
                        if index==2:
                            if screens[index].gameData!=None:
                                gameData=screens[index].gameData
                            print("test")
                            #get the users from createusers and pass them through to randomstartpos
                            
                        # hier moet een aanpassing gemaakt worden wegens het nu via json opsturen van de gebruikers
                        if index == 3:
                            listUsers = gameData['users']
                            res = []
                            for val in listUsers: 
                                if val != None and val!='' : 
                                    res.append(val) 
                            screens[index].spelers=res
                        if index==4:
                            SetupPage3()
                        if index==4:
                            SetupPage4()
                        
                        pageSetup=True
                else:
                    screens[index].shown=False
                    index=5
                    print('Alcohol isnt allowed so dont go to the drink rad')
             
                if index==5:
                    currentAnswer=screens[4].ingevuldAntwoord
                    screens[5].antwoord=currentAnswer
                    # print(currentAnswer)
                if index==6:
                    questionAnsweredCorrect=currentAnswer==screens[5].goede_antwoord
                    screens[6].answeredCorrect=questionAnsweredCorrect
                screens[index].draw()
                    
        except Exception, e:
            #exception was thrown go back to last page
            if index>6:
                index=5
                screens[index].shown=True
                print('index higher then 6 is out of range so go to next question')
            if(index>0):
                index-=1
                screens[index].shown=True
            else:
                index=0
                screens[index].shown=True
            print(str(e))
            traceback.print_exc()

def mousePressed():
    global screens
    try:
        screens[index].mousePressed()
    except Exception as e:
        pass
        # print('mousepressed caused error in: '+str(screens[index])+' --- ignored\n'+str(e))
        # traceback.print_exc()
            
def mouseClicked():
    global screens
    try:
        screens[index].mouseClicked()
    except Exception as e:
        pass
        # print('mouseClicked caused error in: '+str(screens[index])+' --- ignored\n'+str(e))
        # traceback.print_exc()

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
    try:
        screens[index].mouseReleased()
    except Exception, e:
        pass
        # print('mousereleased caused error in: '+str(screens[index])+' --- ignored'+str(e))
        # traceback.print_exc()
            
            
def keyPressed():
    global index,screens,goBack,gameData
    if key==TAB and index>0:
        goBack=True
    try:
        screens[index].keyPressed()
            
    except Exception as e:
        pass
        # print('keyPressed caused error in: '+str(screens[index])+' --- ignored\n'+str(e))    
        # traceback.print_exc()
