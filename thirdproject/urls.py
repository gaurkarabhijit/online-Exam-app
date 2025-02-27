"""
URL configuration for thirdproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from getpass import getuser
from django.contrib import admin
from django.urls import path
# from thirdapp.models import 
from thirdapp.models import student1 # type: ignore
from thirdapp.views import addquestion, adduser, countmque, deleteUser,deleteque, getUser, getallQuestion, getallUser, getpythonqno, hello,display,addQuestion, login, nextQuestion, startest, UpdateQuestion,updateQuestion, updateuser,viewQuestion,deleteQuestion,giveMeregister,giveMelogin,register,previousQuestion,endexam,startest,AdminDash,AdminLogin,ExamScores,AdminToLogin
from thirdapp.views import UpdateQuestion


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello),
    path('display/',display),
    path('addQuestion/',addQuestion),
    path('viewQuestion/',viewQuestion),
    path('deleteQuestion/',deleteQuestion),
    path('giveMeregister/',giveMeregister),
    path('giveMelogin/',giveMelogin),
    path('login/',login),
    path('register/',register),
    path('nextQuestion/',nextQuestion),
    path('previousQuestion/',previousQuestion),
    path('endexam/',endexam),
    path('starttest/',startest),
    path('AdminDash/',AdminDash),
    path('AdminLogin/',AdminLogin),
    path('ExamScores/',ExamScores),
    path('AdminToLogin/',AdminToLogin),
    path('getallQuestion/',getallQuestion),
    path('getpythonqno/',getpythonqno),
    path('deleteque/<subfromuser>/<qnofromuser>/',deleteque),
    path('UpdateQuestion/',UpdateQuestion),
    path('countmque/<subfrombrowser>/',countmque),
    # path('student/',student),
    path('adduser/',adduser),
    path('addquestion/',addquestion),
    path('Updateuser/',updateuser),
    path('updateQuestion/',updateQuestion),
    path('getallUser/',getallUser),
    path('getUser/<username>',getUser),
    path('deleteUser/<userfromclient>',deleteUser)
    

]
