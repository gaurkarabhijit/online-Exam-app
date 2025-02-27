from django.contrib import admin

from thirdapp.models import Question,UserData

admin.site.register(Question)
admin.site.register(UserData)

# Register your models here.
