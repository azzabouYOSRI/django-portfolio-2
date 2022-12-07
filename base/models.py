import numbers

from django.core.exceptions import ValidationError
from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
        primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(null=True, default="skill.png")
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
        primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    lastname = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False)
    subject = models.CharField(max_length=200, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Refrence(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    lastname = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False)
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'refrence'

    def __str__(self):
        return self.body[0:50]


class Awardsandhonors(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(null=True, default="skill.png")
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    Date_recived = models.DateTimeField()

    def __str__(self):
        return self.title


class Transcript(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    logo = models.ImageField(null=True, default="skill.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


class Communityservice(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    logo = models.ImageField(null=True, default="skill.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


def validate_only_one_instanceOfMissionstatement(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class Missionstatement(models.Model):
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    id = numbers

    def clean(self):
        validate_only_one_instanceOfMissionstatement(self)


def validate_only_one_instanceOfPersonalinfomation(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class Personalinfomation(models.Model):
    id = numbers
    name = models.CharField(max_length=100, null=True, blank=False)
    lastname = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(max_length=50, unique=True, null=True, blank=False)
    function = models.CharField(max_length=100, null=True, blank=True)
    slogan = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def clean(self):
        validate_only_one_instanceOfPersonalinfomation(self)
