from urllib import request

from django.shortcuts import render, redirect

from .forms import ProjectForm, MessageForm, SkillForm, MissionForm
# , redirect
from .models import Project, Skill, Message, Missionstatement
# , Message, Endorsement
# from .forms import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm, QuestionForm
from django.contrib import messages

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')

    skills = Skill.objects.filter(body='')
    mission = Missionstatement.objects.first()
    # endorsements = Endorsement.objects.filter(approved=True)

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You message was successfully sent!.')

    # context = {
    #            , , 'endorsements': endorsements}
    context = {'projects': projects,'skills': skills,'detailedSkills': detailedSkills, 'form': form, 'mission': mission}
    return render(request, 'base/home.html', context)






def profilpage(request):

    context = {}
    return render(request, 'base/internal/Profile-page.html', context)




def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'base/internal/project.html', context)


def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/forms/project_form.html', context)

def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/forms/project_form.html', context)
def deleteproject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Your project was successfully deleted!')
        return redirect('home')
    context = context = {'project' :project}

    return render(request, 'base/internal/delete/delete-Project.html', context)




def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')

    unreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadCount': unreadCount}
    return render(request, 'base/internal/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'base/internal/message.html', context)


def addSkill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Your skill was successfully added!')
        return redirect('home')
    context = {'form': form}
    return render(request, 'base/forms/skill_form.html', context)

def editskills(request, pk):
    skill = Skill.objects.get(id=pk)
    form = ProjectForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/forms/skill_form.html', context)
def deleteskill(request, pk):
    skill = Skill.objects.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Your skill was successfully deleted!')
        return redirect('home')
    context = context = {'skill' :skill}

    return render(request, 'base/internal/delete/delete-Skill.html', context)










def addmission_statment(request):
    form = MissionForm()
    b : bool  = False
    if request.method == 'POST' and b == False:
        form = MissionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Your skill was successfully added!')
        b = True
        return redirect('home')
    context = {'form': form}
    return render(request, 'base/forms/mission_form.html', context)

def editmission(request, pk):
    mission = Missionstatement.objects.get(id=pk)
    form = ProjectForm(instance=mission)

    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=mission)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/forms/mission_form.html', context)
def deletemission(request, pk):
    skill = Skill.objects.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Your skill was successfully deleted!')
        return redirect('home')
    context = context = {'skill' :skill}

    return render(request, 'base/internal/delete/delete-mission.html', context)







# def addEndorsement(request):
#     form = EndorsementForm()
#     if request.method == 'POST':
#         form = EndorsementForm(request.POST)
#         form.save()
#         messages.success(
#             request, 'Thank you, your endorsement was successfully added!')
#         return redirect('home')
#     context = {'form': form}
#     return render(request, 'base/endorsement_form.html', context)
#
#
# def donationPage(request):
#     return render(request, 'base/donation.html')
#
#
# def chartPage(request):
#     form = QuestionForm()
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         form.save()
#         messages.success(
#             request, 'Thank you your vote!')
#         return redirect('chart')
#     return render(request, 'base/chart.html', {'form': form})
