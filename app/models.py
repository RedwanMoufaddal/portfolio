from django.db import models

# Create your models here.

class Base(models.Model):
    bg_img = models.FileField(upload_to="img" )
    linkdin_link = models.URLField(max_length=200)
    twiter_link = models.URLField(max_length=200)
    instagram_link = models.URLField(max_length=200)
    youtube_link = models.URLField(max_length=200)
    my_phone = models.CharField( max_length=100)
    my_gmail = models.EmailField( max_length=254)
    class Meta:
        verbose_name = ("Base")
        verbose_name_plural = ("Bases")



class Project(models.Model):
    img_projects = models.FileField( upload_to="img")
    title_projects = models.CharField(max_length=100)
    petit_desc_projects = models.CharField(max_length=190)
    link_git_project = models.URLField( max_length=300)
    
    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")



class Services(models.Model):
    icon_server_fontawesome_class = models.CharField( default='class="fas fa-edit"',max_length=200)
    title_service = models.CharField( max_length=100)
    desc_service = models.CharField( max_length=500)
    
    class Meta:
        verbose_name = ("Services")
        verbose_name_plural = ("Servicess")

