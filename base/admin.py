from django.contrib import admin

# Register your models here.

from .models import Project, Skill, Message, Refrence, Missionstatement,Personalinfomation,Transcript,Awardsandhonors,Communityservice

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Message)
admin.site.register(Missionstatement)
admin.site.register(Refrence)
admin.site.register(Personalinfomation)
admin.site.register(Transcript)
admin.site.register(Awardsandhonors)
admin.site.register(Communityservice)
