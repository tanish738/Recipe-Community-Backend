from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

#for token 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


#this function goes to static/images as that is the MEDIA_ROOT in settings.py
#it then uploads images of users in a dir userProfile/<userEmail>/<uploaded_image>
def upload_path_handler(instance, filename): 
    return "userProfile/{title}/{file}".format(
        title=instance.myUser.email, file=filename
    )


class MyUser(AbstractUser):
    email           = models.EmailField(unique=True, blank = False)
    username        = models.CharField(max_length = 100,unique=True, blank = False)
    first_name      = models.CharField(max_length = 100, blank = True)
    last_name       = models.CharField(max_length = 100, blank = True)
    profile_picture = models.ImageField(default = "default_user_profile.png", upload_to = upload_path_handler) 
    Created         = models.DateTimeField(null = True, blank = False, auto_now_add = True)
    # KEEP IT DEFAULT TRUE
    is_active       = models.BooleanField(default = True) #so that we can activate using SMTP # keep it true until running the server
    is_chef         = models.BooleanField(default = False) #for V2
    bio             = models.TextField(blank = True)
    slug            = models.SlugField(max_length=100, unique=True)

    USERNAME_FIELD = 'email' #login signup with email instead of username
    REQUIRED_FIELDS=['username']#admin creation
    

    def __str__(self):
        return self.email


    #will display a summary of bio upto 50 words
    def summary(self): 
        return self.bio[:50] + "..."
    
    
    #save the slug field before saving myUser model
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(MyUser, self).save(*args, **kwargs)

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        token=Token.objects.create(user = instance)


