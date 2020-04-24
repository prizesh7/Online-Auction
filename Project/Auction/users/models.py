from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(max_length=10, blank=True)
    pla_auc = models.CharField(max_length=50,default="no",choices=[('no', 'no'),('yes', 'yes')])    

    def __str__(self):
        return f'{self.user.username} Profile'

    #def save(self, *args, **kawrgs):
    #    super().save(*args, **kawrgs)

     #   img = Image.open(self.image.path)

      #  if img.height > 300 or img.width > 300:
       #     output_size = (300, 300)
        #    img.thumbnail(output_size)
         #   img.save(self.image.path)
