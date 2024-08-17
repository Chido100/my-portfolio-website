from django.db import models
import PIL



class Dashboard(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_image')
    intro = models.TextField(default='Hi there...')

    class Meta:
        verbose_name_plural = 'Dashboard'

    def __str__(self):
        return self.name


class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_image = models.ImageField(upload_to='skill_images')

    class Meta:
        verbose_name_plural = 'Skills'


    def __str__(self):
        return self.skill_name


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images', default='')
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class About(models.Model):
    summary = models.TextField()

    class Meta:
        verbose_name_plural = 'About'
        

    def __str__(self):
        return self.summary


class ContactMe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Contact Me'

    def __str__(self):
        return self.subject

