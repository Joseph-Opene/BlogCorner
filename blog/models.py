'''
shows and creates stuffs you want to sell or do
products, blogs and all that... And don't forget to make migrations after each model you make
to register it in the database.
'''

from django.db import models
#we import timezone so we can update the dates anytime when we want to, and set the date posted to default=timezone.now
from django.utils import timezone
from django.contrib.auth.models import User
#we set the user to foreignkey because 1 user can have mulitple post but 1 post can have only 1 user in the database relationship
#CASCADE helps us to delete all post relating to a user when we delete the user
from django.urls import reverse

class Post(models.Model):


    title = models.CharField(max_length=100)
    content = models.TextField()
    number_of_likes = models.IntegerField(default=0)
    number_of_shares = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

#we want our post to be more descriptive we use the dunda(str) method, and here we just want to display just the title
    def __str__(self):
        return self.title
#Methods to find a specific post. Geeting the url for a specific route... We import the reverse module
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

#adding the like button and like counter to our blog
class Likes(models.Model):


    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    time_liked = models.DateTimeField(default=timezone.now)
    liked_by = models.IntegerField(blank=False)

    def __str__(self):
        return f"Likes({self.post.id}, {self.liked_by})"


class Share(models.Model):


    post = models.ForeignKey(Post, related_name='shares', on_delete=models.CASCADE)
    shared_by = models.IntegerField(blank=False)
    quote = models.CharField(max_length=255, blank=True,default='')
    time_shared = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Share({self.post.title}, {self.shared_by})"
'''
class Comment(models.Model):


    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255,blank=False)
    commented_by = models.ForeignKey(User,related_name='my_comments', on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=timezone.now)
    replying_to = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment({self.post.title}, {self.comment})"
'''
