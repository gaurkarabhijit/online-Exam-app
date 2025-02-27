from urllib import request, response
from django.shortcuts import render
from django.http import HttpResponse

from thirdapp.models import Question, UserData,result,admin, student1 # type: ignore


# Create your views here.

def hello(request):
    return HttpResponse("welcome")


def display(request):
    return render(request,'questionmanagement.html')


def addQuestion(request):
     
      Question.objects.create(qno=request.GET["qno"],qtext=request.GET["qtext"],answer=request.GET["answer"],op1=request.GET["op1"],op2=request.GET["op2"],op3=request.GET["op3"],op4=request.GET["op4"],subject=request.GET["subject"])

      return render(request,'questionmanagement.html',{'message':'Question Added Successfully'})


    
def viewQuestion(request):
     
     question=Question.objects.get(qno=request.GET["qno"],subject=request.GET["subject"])
     return render(request,'questionmanagement.html',{'question':question})

def deleteQuestion(request):
     Question.objects.filter(qno=request.GET["qno"],subject=request.GET["subject"]).delete()
     return render(request,'questionmanagement.html',{'message':'record deleted'})


def UpdateQuestion(request):

    question = Question.objects.filter(qno=request.GET["qno"], subject=request.GET["subject"])

    question.update(
                qtext=request.GET['qtext'],
                answer=request.GET['answer'],
                op1=request.GET['op1'],
                op2=request.GET['op2'],
                op3=request.GET['op3'],
                op4=request.GET['op4'],
        )
    return render(request, 'questionmanagement.html', {'message': "Question update successfully"})


def giveMelogin(request):
     return render(request,'login.html')

def giveMeregister(request):
     return render(request,'register.html')


def register(request):

    usernamefrombrowser=request.GET["username"] 
    passfrombrowser=request.GET["password"]
    mobileno=request.GET["mobno"]

    # create method will save given details in database table userdata . it will generate and execute insert query

    UserData.objects.create(username=usernamefrombrowser,password=passfrombrowser,mobno=mobileno)

   # create() will create new row in database table

    #print(connection.queries)

    return render(request,"login.html",{'message':"registration successful . please login now"})

def login(request):
    
    usernamefrombrowser=request.GET["username"] 
    passfrombrowser=request.GET["password"] 

    request.session["username"]=usernamefrombrowser

    # {username=tka} session dictionary

    try:
        userfromdatabase=UserData.objects.get(username=usernamefrombrowser) # get() will give object from Database
    except:
        return render(request,"login.html",{'message':"Invalid username"})
    
   # print(connection.queries)
    
    # userfromdatabase==> [username=tka  password=tkakiranacademy mobno=12345] UserData class's object is given by get() method

    if userfromdatabase.password == passfrombrowser:
        
        request.session['answers'] = {}
        request.session['score'] = 0
        request.session["qno"]=-1
       
        # queryset=Question.objects.filter(subject='math').values()
        # listofquestions=list(queryset)
        # request.session["listofquestions"]=listofquestions

        return render(request,"subject.html",{'message':"welcome " + usernamefrombrowser})
    
    
    #serilizable
    
    else:

        return render(request,"login.html",{'message':"Invalid password..",'oldusername':usernamefrombrowser})
    
def startest(request):
     subjectname=request.GET['subject']
     request.session['subject']=subjectname

     queryset=Question.objects.filter(subject=subjectname).values()
     listofquestions=list(queryset)

     request.session["listofquestions"]=listofquestions

     return render(request,"questionnavigation.html", {'question':listofquestions[0]})


def nextQuestion(request):
    if 'op' in request.GET:

        allanswers=request.session['answers']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

        # allanswers  {'1':[1,'what','a','c'],'2' : ['2','why','d','d']}

        print(allanswers)

    
    allquestions=request.session["listofquestions"]

    questionindex=request.session['qno']
    
    if questionindex<len(allquestions)-1:

        request.session["qno"]=request.session["qno"] + 1
    
        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session["qno"]]

    else:

        return render(request,'questionnavigation.html',{'message':"click on previous",'question':allquestions[len(allquestions)-1]})

    return render(request,'questionnavigation.html',{'question':question})

    # qno=qno+1



def previousQuestion(request):
    if 'op' in request.GET:

        allanswers=request.session['answers']

        allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

        print(allanswers)

    allquestions=request.session["listofquestions"]
    questionindex=request.session['qno']

    if questionindex>0:

        request.session["qno"]=request.session["qno"] - 1
    
        print(f"qno is {request.session['qno']}")

        question=allquestions[request.session["qno"]]

    else:

        return render(request,'questionnavigation.html',{'message':"click on next",'question':allquestions[0]})

    return render(request,'questionnavigation.html',{'question':question})


def endexam(request):

        if 'op' in request.GET:

            allanswers=request.session['answers'] # {}

            allanswers[request.GET['qno']]=[request.GET['qno'],request.GET['qtext'],request.GET['answer'],request.GET['op']]

            print(allanswers)


        responses=request.session['answers']
        allanswers2=responses.values()
        
        for ans in allanswers2:
        
            print(f'correct answer {ans[2]}  and submitted answer is {ans[3]}') 
            
            if ans[2]==ans[3]:
                    request.session['score']=request.session['score'] + 1

        finalscore=request.session['score']
        print(f'Your score is {finalscore}')    

        usernamefrombrowser=request.session.get('username')    
        subjectname=request.session.get('subject')

        if usernamefrombrowser and subjectname:
             result.objects.create(username=usernamefrombrowser, subject=subjectname,score=finalscore)
        else:
             print("Error: Username or subject is missing.")

        return render(request, 'score.html',{'score':finalscore,'responses':allanswers2})
                
        # try:
        #     Result.objects.create(username=request.session['username'],subject=request.session['subject'],score=finalscore)
        # except:
        #     return render(request,'login.html')    



def AdminLogin(request):
    return render(request,'adminLogin.html')

def AdminToLogin(request):
    adminnamefrombrowser=request.GET['adminname']
    passfrombrowser=request.GET['password']

    request.session['adminname']=adminnamefrombrowser

    try:
        adminnamefromdb=admin.objects.get(username=adminnamefrombrowser)
    except:
        return render(request, 'login.html',{'message': 'invalid username'})


    if adminnamefromdb.password == passfrombrowser:

        return render(request,"adminDash.html", {"message":"welcome" + "\t" +  adminnamefrombrowser})

    else:
        return render(request,"adminlogin.html",{"message":"Invalid Credential"})



def AdminDash(request):
    return render(request,'adminDash.html')

def ExamScores(request):
    Results=result.objects.all()
    return render(request,'examscores.html',{'Results':Results})

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getallQuestion(request):
    queryset = Question.objects.all().values() # type: ignore
    listofQuestion = list(queryset)
    return Response(listofQuestion)


@api_view(['GET'])
def getpythonqno(request):
    questions=Question.objects.filter(subject="Python")

    pythonq=list(questions.values())
    return Response(pythonq)

@api_view(['DELETE'])
def deleteque(request,subfromuser,qnofromuser):  
    try:
        ques=Question.objects.filter(subject=subfromuser,qno=qnofromuser)
        if ques.exists():
            ques.delete()
            return Response({'message':'question deleted'})
        else:
            return Response({'message':'does not exist'})
    except Exception as e:
        return Response({'error':'an error occure'})
    


@api_view(['GET'])
def countmque(request,subfrombrowser):
    question=Question.objects.filter(subject=subfrombrowser)
    if question.exists():
        questionno=list(question)
        return Response(len(questionno))


    return Response({'message': 'question number is empty' })

# def student(request):
    # return render(request,'student.html')


@api_view(['POST'])
def adduser(request):

    print(request.data)
    userfromclient=request.data
    UserData.objects.create(username = userfromclient['username'],mobno=userfromclient['mobno'],password=userfromclient['password'])
    response = Response(userfromclient)
    return response

@api_view(['GET'])
def getallUser(request):
    queryset=UserData.objects.all().values()
    listofuser=list(queryset)
    return Response(listofuser)


@api_view(['GET'])
def getUser(request,username):

    userfromdb=UserData.objects.get(username=username)
    response=Response({'username':userfromdb.username,'password':userfromdb.password,'mobno':userfromdb.mobno})
    return response

@api_view(['POST'])
def addquestion(request):

    print(request.data)
    userfromclient=request.data
    Question.objects.create(qno=userfromclient['qno'],qtext=userfromclient['qtext'],answer=userfromclient['answer'],op1=userfromclient['op1'],op2=userfromclient['op2'],op3=userfromclient['op3'],op4=userfromclient['op4'],subject=userfromclient['subject'])
    response= Response(userfromclient)
    return response


@api_view(['PUT'])
def updateuser(request):
    dictionary=request.data
    usrfromdb=UserData.objects.get(username=dictionary["username"])
    usrfromdb.password=dictionary["password"]
    usrfromdb.mobno=dictionary["mobno"]
    usrfromdb.save()
    return Response(dictionary)

@api_view(['DELETE'])
def deleteUser(request, userfromclient):
    user = UserData.objects.filter(username=userfromclient)
    
    if user.exists():
        user.delete()
        return Response({'message': 'Record deleted'})
    
    return Response({'message': 'Invalid username'})


@api_view(['PUT'])
def updateQuestion(request):

    data=request.data
    userfromdb=Question.objects.get(qno=data['qno'])
    userfromdb.qtext=data['qtext']
    userfromdb.answer=data['answer']
    userfromdb.op1=data['op1']
    userfromdb.op2=data['op2']
    userfromdb.op3=data['op3']
    userfromdb.op4=data['op4']
    userfromdb.subject=data['subject']
    userfromdb.save()
    return Response(data)



