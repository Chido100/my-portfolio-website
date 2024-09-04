from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model


User = get_user_model()



class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog_image')
    blog_body = RichTextField(verbose_name='Blog Body')
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title



    


