from django.db import models
from django.db import IntegrityError


class Profile(models.Model):
    full_name=models.CharField(max_length=200, help_text='Enter full name')
    title=models.CharField(max_length=200, help_text='Enter titles putting comma between them')
    social_twitter=models.CharField(max_length=200)
    social_facebook = models.CharField(max_length=200)
    social_linkedin = models.CharField(max_length=200)
    social_website=models.URLField()
    phone_number=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    project_completed=models.IntegerField(default=0)
    happy_client = models.IntegerField(default=0)
    years_of_experience = models.IntegerField(default=0)
    hobby=models.CharField(max_length=200, help_text='Enter hobbies putting commas in between them', blank=True)

    def __str__(self):
        return self.full_name

    def get_first_name(self):
        return self.full_name


class Skill(models.Model):
    name=models.CharField(max_length=200)
    progress_level=models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Project(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    url_link=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name


class Testimony(models.Model):
    full_name=models.CharField(max_length=1000)
    content=models.TextField()
    job=models.CharField(max_length=1000)

    def __str__(self):
        return self.full_name


class Message(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=2000)

    def __str__(self):
        return self.subject

    @classmethod
    def create_message(cls, **kwargs):
        try:
            return cls.objects.create(**kwargs)
        except IntegrityError:
            return None

















