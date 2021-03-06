<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):
        def get_queryset(self):
            return super(UserProfileManager, self).get_queryset().order_by('user__username')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default ='')
    website = models.URLField(default ='')
    image = models.ImageField(upload_to='profile_image')
    def __str__(self):
        return self.user.username






def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
=======
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):
        def get_queryset(self):
            return super(UserProfileManager, self).get_queryset().order_by('user__username')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default ='')
    website = models.URLField(default ='')
    image = models.ImageField(upload_to='profile_image')
    def __str__(self):
        return self.user.username






def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
>>>>>>> e854a0e1d078f16e921a24a3e201c203befc9c4a
