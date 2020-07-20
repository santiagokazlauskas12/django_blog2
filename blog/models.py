from django.db import models
from ckeditor.fields  import RichTextField 
from django.contrib.auth.models import User
from django.utils import timezone

class Post (models.Model):
    author=models.ForeignKey(User, verbose_name=("user"), null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200,verbose_name="Titutlo :")  
    text=RichTextField(verbose_name="Contenido :" )
    created_at=models.DateTimeField(auto_now=True, verbose_name="Created at :")
    published_at=models.DateTimeField(blank=True,null=True)


    def published (self):
        self.published_at= timezone.now() 
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


    def __str__(self):
        return self.title
        
    

class Comment (models.Model):
    post=models.ForeignKey(Post,related_name='comment', on_delete=models.CASCADE)
    author=models.CharField(verbose_name="author :", max_length=200)
    text=RichTextField(verbose_name="comment :" )
    created_at=models.DateTimeField(auto_now=True)
    aproved=models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


    def aprove (self):
        self.aproved=True 
        self.save()   
    

         