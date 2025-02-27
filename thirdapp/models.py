from django.db import models

# Create your models here.
class Question(models.Model):
    
    qno=models.IntegerField(primary_key=True)
    qtext=models.CharField(max_length=100)
    answer=models.CharField(max_length=50)
    op1=models.CharField(max_length=50)
    op2=models.CharField(max_length=50)
    op3=models.CharField(max_length=50)
    op4=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.qno , self.qtext , self.answer,self.op1,self.op2}"
    
    class Meta:
        db_table="question"

class UserData(models. Model):
    username=models.CharField(max_length=20, primary_key=True)
    password=models.CharField(max_length=20)
    mobno=models.IntegerField()
    

    

    def __str__(self):
         return f"username is {self.username} and password is {self.password} and mobno {self.mobno} "


    class Meta:
        db_table="userdata"

class result(models.Model):

    username=models.CharField(max_length=20,primary_key=True)
    subject=models.CharField(max_length=20)
    score=models.IntegerField()

    class Meta:
        db_table="result"

class admin(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)



    class Meta:
        db_table="admin"

class student1(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    email=models.CharField(max_length=200, unique=True)
    mobile=models.IntegerField()
    dob=models.DateField(default=1/2/2024)
    course=models.CharField(max_length=50)
    percentages=models.FloatField()
    year_of_study=models.IntegerField()

    class Meta:
        db_table="student1"

def __str__(self):
    return f"{self.username} - {self.course}"


class Card(models.Model):
    # Fields inside the model
    name = models.CharField(max_length=100)





    







