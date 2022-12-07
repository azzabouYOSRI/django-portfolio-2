from urllib import request

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ProjectForm, MessageForm, SkillForm, MissionForm, Communityservicefrom, \
    Awardsandhonorsform, Personalinfomationform, Transcriptform, Refrenceform, CustomUserCreationForm
from .models import Project, Skill, Message, Missionstatement, Communityservice, Awardsandhonors, Personalinfomation, Transcript, Refrence
from django.contrib import messages


# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    personalinfomations = Personalinfomation.objects.all()
    transcripts = Transcript.objects.all()
    refrences = Refrence.objects.all()
    communityservices = Communityservice.objects.all()
    awardsandhonorss = Awardsandhonors.objects.all()
    detailedSkills = Skill.objects.exclude(body='')

    skills = Skill.objects.filter(body='')
    mission = Missionstatement.objects.first()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You message was successfully sent!.')
    context = {'projects': projects, 'skills': skills, 'detailedSkills': detailedSkills, 'form': form,
               'mission': mission , 'personalinfomations':personalinfomations , 'transcripts':transcripts , 'refrences':refrences , 'communityservices':communityservices , 'awardsandhonorss':awardsandhonorss}
    return render(request, 'base/home.html', context)


def profilpage(request):
    personalinfomations = Personalinfomation.objects.all()
    context = {'personalinfomations': personalinfomations}
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
    context = context = {'project': project}

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
        form = SkillForm(request.POST, request.FILES)
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
    context = context = {'skill': skill}

    return render(request, 'base/internal/delete/delete-Skill.html', context)


def addmission_statment(request):
    form = MissionForm()
    b: bool = False
    if request.method == 'POST' and b == False:
        form = MissionForm(request.POST, request.FILES)
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
        form = MissionForm(request.POST, request.FILES, instance=mission)
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
    context = context = {'skill': skill}

    return render(request, 'base/internal/delete/delete-mission.html', context)


def addPersonalinfomation(request):
    form = Personalinfomationform()

    if request.method == 'POST':
        form = Personalinfomationform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,
                  'base/forms/Personalinfomation_form.html',
                  context)


def editPersonalinfomation(request, pk):
    personalinfomation = Personalinfomation.objects.get(id=pk)
    form = Personalinfomationform(instance=personalinfomation)

    if request.method == 'POST':
        form = Personalinfomationform(request.POST, request.FILES, instance=Personalinfomation)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,
                  'base/forms/Personalinfomation_form.html',
                  context)


def deletePersonalinfomation(request, pk):
    personalinfomation = Personalinfomation.objects.get(id=pk)

    if request.method == 'POST':
        personalinfomation.delete()
        messages.success(request, 'Your Personalinfomation was successfully deleted!')
        return redirect('home')
    context = context = {'Personalinfomation': Personalinfomation}

    return render(request,
                  'base/internal/delete/delete-Personalinfomation.html',
                  context)


def addTranscript(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = Transcriptform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,
                  'base/forms/Transcript_form.html',
                  context)


def editTranscript(request, pk):
    transcript = Transcript.objects.get(id=pk)
    form = Transcriptform(instance=Transcript)

    if request.method == 'POST':
        form = Transcriptform(request.POST, request.FILES, instance=transcript)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,
                  'base/forms/Transcript_form.html',
                  context)


def deleteTranscript(request, pk):
    transcript = Transcript.objects.get(id=pk)

    if request.method == 'POST':
        transcript.delete()
        messages.success(request, 'Your Transcript was successfully deleted!')
        return redirect('home')
    context = context = {'Transcript': Transcript}

    return render(request,
        'base/internal/delete/delete-Transcript.html',
        context)


def addrefrence(request):
    form = Refrenceform()

    if request.method == 'POST':
        form = Refrenceform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/forms/endorsement_form.html', context)


def editrefrence(request, pk):
    refrence = Refrence.objects.get(id=pk)
    form = Refrenceform(instance=refrence)

    if request.method == 'POST':
        form = Refrenceform(request.POST, request.FILES, instance=refrence)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/forms/endorsement_form.html', context)


def deleterefrence(request, pk):
    refrence = Refrence.objects.get(id=pk)

    if request.method == 'POST':
        refrence.delete()
        messages.success(request, 'Your endorsement was successfully deleted!')
        return redirect('home')
    context = context = {'refrence': refrence}

    return render(request,
                  'base/internal/delete/delete-Endorsement.html',
                  context)


def Addcommunityservice(request):
    form = Communityservicefrom()

    if request.method == 'POST':
        form = Communityservicefrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,
                  'base/forms/Communityservice_form.html',
                  context)


def editCommunityservice(request, pk):
    communityservice = Communityservice.objects.get(id=pk)
    form = Communityservicefrom(instance=communityservice)

    if request.method == 'POST':
        form = Communityservicefrom(request.POST, request.FILES, instance=Communityservice)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,
                  'base/forms/Communityservice_form.html',
                  context)


def deleteCommunityservice(request, pk):
    communityservice = Communityservice.objects.get(id=pk)

    if request.method == 'POST':
        communityservice.delete()
        messages.success(request, 'Your Community service was successfully deleted!')
        return redirect('home')
    context = context = {'Communityservice': Communityservice}

    return render(request,
                  'base/internal/delete/delete-Communityservice.html',
                  context)


def addAwardsandhonors(request):
    form = Awardsandhonorsform()

    if request.method == 'POST':
        form = Awardsandhonorsform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,
                  'base/forms/Awardsandhonors_form.html',
                  context)


def editAwardsandhonors(request, pk):
    awardsandhonors = Awardsandhonors.objects.get(id=pk)
    form = Awardsandhonorsform(instance=awardsandhonors)

    if request.method == 'POST':
        form = Awardsandhonorsform(request.POST, request.FILES, instance=awardsandhonors)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,
                  'base/forms/Awardsandhonors_form.html',
                  context)


def deleteAwardsandhonors(request, pk):
    awardsandhonors = Awardsandhonors.objects.get(id=pk)

    if request.method == 'POST':
        awardsandhonors.delete()
        messages.success(request, 'Your Awards and honors was successfully deleted!')
        return redirect('home')
    context = context = {'Awardsandhonors': Awardsandhonors}

    return render(request,
                  'base/internal/delete/delete-Awardsandhonors.html',
                  context)

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'base/login_register.html', {'page': page})



def logoutUser(request):
    logout(request)
    return redirect('login')


def updateUser(request,pk):
    user = User.objects.get(id=pk)
    page = 'update'
    form = CustomUserCreationForm(instance=user)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('profile')

    context = {'form': form, 'page': page}
    return render(request, 'base/login_register.html', context)
