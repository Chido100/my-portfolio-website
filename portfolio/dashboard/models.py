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


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    duty = models.TextField()


    def __str__(self):
        return self.company_name


class Project(models.Model):
    title = models.CharField(max_length=255)
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


