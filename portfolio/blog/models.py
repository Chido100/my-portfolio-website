from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model


User = get_user_model()



class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog_image')
    blog_intro = models.TextField(verbose_name='Blog Introduction')
    blog_body = RichTextField(verbose_name='Blog Body')
    blog_closure = models.TextField(verbose_name='Blog Closure')
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title



    


