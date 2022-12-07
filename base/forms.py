from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Project, Message, Skill, Missionstatement, Personalinfomation, Refrence, Transcript, Awardsandhonors, \
    Communityservice
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'body']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['thumbnail'].widget.attrs.update(
            {'class': 'form-control', })


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['lastname'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', })

        self.fields['subject'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['logo'].widget.attrs.update(
            {'class': 'form-control', })


class MissionForm(ModelForm):
    class Meta:
        model = Missionstatement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MissionForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update(
            {'class': 'form-control'})


class Personalinfomationform(ModelForm):
    class Meta:
        model = Personalinfomation
        fields = ['name', 'lastname', 'email','function','slogan','password','profile_picture']

    def __init__(self, *args, **kwargs):
        super(Personalinfomationform, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['lastname'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['function'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['slogan'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['profile_picture'].widget.attrs.update(
            {'class': 'form-control', })


class Refrenceform(ModelForm):
    class Meta:
        model = Refrence
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Refrenceform, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['lastname'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['thumbnail'].widget.attrs.update(
            {'class': 'form-control', })


class Transcriptform(ModelForm):
    class Meta:
        model = Transcript
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Transcriptform, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['logo'].widget.attrs.update(
            {'class': 'form-control', })


class Awardsandhonorsform(ModelForm):
    class Meta:
        model = Awardsandhonors
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Awardsandhonorsform, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['logo'].widget.attrs.update(
            {'class': 'form-control', })


class Communityservicefrom(ModelForm):
    class Meta:
        model = Communityservice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Communityservicefrom, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['logo'].widget.attrs.update(
            {'class': 'form-control', })


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm password...'})
