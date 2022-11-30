from django.forms import ModelForm
from .models import Project, Message, Skill, Missionstatement, User, Refrence, Transcript, Awardsandhonors, \
    Communityservice


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


class Userform(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)
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
















# from django.forms import ModelForm
# from .models import Project, Message, Skill, Missionstatement, User, Refrence, Transcript, Awardsandhonors, \
#     Communityservice
#
#
# class ProjectForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['title', 'thumbnail', 'body']
#
#     def __init__(self, *args, **kwargs):
#         super(ProjectForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update(
#             {'class': 'form-control'})
#
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['thumbnail'].widget.attrs.update(
#             {'class': 'form-control', })
#
#
# class MessageForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = '__all__'
#         exclude = ['is_read']
#
#     def __init__(self, *args, **kwargs):
#         super(MessageForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['lastname'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['email'].widget.attrs.update(
#             {'class': 'form-control', })
#
#         self.fields['subject'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control', })
#
#
# class SkillForm(ModelForm):
#     class Meta:
#         model = Skill
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(SkillForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['logo'].widget.attrs.update(
#             {'class': 'form-control', })
#
#
# class MissionForm(ModelForm):
#     class Meta:
#         model = Missionstatement
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(MissionForm, self).__init__(*args, **kwargs)
#         self.fields['content'].widget.attrs.update(
#             {'class': 'form-control'})
#
# class Userform(ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(Userform, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['lastname'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['email'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['function'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['slogan'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['password'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['profile_picture'].widget.attrs.update(
#             {'class': 'form-control', })
#
#
# class Refrenceform(ModelForm):
#     class Meta:
#         model = Refrence
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(Refrenceform, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['lastname'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['email'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['phone'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['title'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control', })
#         self.fields['thumbnail'].widget.attrs.update(
#             {'class': 'form-control', })
#
#
# class Transcriptform(ModelForm):
#     class Meta:
#         model = Transcript
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(Refrenceform, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['logo'].widget.attrs.update(
#             {'class': 'form-control', })
#
#
# class Awardsandhonorsform(ModelForm):
#     class Meta:
#         model = Awardsandhonors
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(Awardsandhonorsform, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['logo'].widget.attrs.update(
#             {'class': 'form-control', })
#
# class Communityservice(ModelForm):
#     class Meta:
#         model = Communityservice
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(Communityservice, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['logo'].widget.attrs.update(
#             {'class': 'form-control', })


# class EndorsementForm(ModelForm):
#     class Meta:
#         model = Endorsement
#         fields = '__all__'
#         exclude = ['featured']
#
#     def __init__(self, *args, **kwargs):
#         super(EndorsementForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control', })
#
#
# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         exclude = ['project']
#
#     def __init__(self, *args, **kwargs):
#         super(CommentForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update(
#             {'class': 'form-control'})
#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control', })
#
#
# class QuestionForm(ModelForm):
#     class Meta:
#         model = Question
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(QuestionForm, self).__init__(*args, **kwargs)
#         self.fields['answer'].widget.attrs.update(
#             {'class': 'form-control'})
