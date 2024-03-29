from django.db import models
from django.contrib.auth.models import User
#we install the pillow library to help us with images
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/images/default_tr5qy7',
    upload_to='images/')

#creating a one to one relationship with user and profile
    def __str__(self):
        return f'{self.user.username} Profile'

#overriding the save method by creating our own so our dp can be resized to smaller pixels to avoid our site running slow
    '''def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

#resizing the images
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)'''


class Gallery(models.Model):
    user = models.ForeignKey(User, related_name='gallery', on_delete=models.CASCADE)
    uploads = models.ImageField(blank=True, upload_to='images/')


    def __str__(self):
        return f"Gallery('{self.user.username}','{self.uploads}')"
