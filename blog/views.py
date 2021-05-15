from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
#We import the get_object_or_404 so when we try to find post for a user that doest exist in our UserPostListView it shows us error 404.
'''we get rid of our dummy data for the posts and import the Post from the models,
and we show the post we made from our command line and pass it into the context as
Post.objects.all()
'''
from .models import Post, Likes
#We import the user as we will be using the user model in our UserPostListView
from django.contrib.auth.models import User
#importing a function that would take us to a particular blog so well see all the content, details and comments. Then change it to our home view in the urls
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#CreateView is for users to be able to create posts from their frontend pages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#The mixin helps us to require login before a post is made and add it to the CreateView.. We use mixins cause we cant use decorators for Class based views.
#We use the PassesTestMixin to makesure it is just the author of the post thats able to edit or update it. And add it to the left after the LoginRequired of our UpdateView

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

#help us see more details of our posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #when we ran the app, it didnt work cause it was looking for this convention, <app>/<model>_<viewtype>.html
    #postlistview sees our post as list so lets change that
    context_object_name = 'posts'
    #ordering so our lastest posts show at the top
    ordering = ['-date_posted']
    #Paginating our posts and breaking them into different pages and sections so we dont have too many at once. So we can set it to 5 post per page
    paginate_by = 5

#When we click on a particular user, to see all his/her posts and parginate them
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #we create the template
    #postlistview sees our post as list so lets change that
    context_object_name = 'posts'
    #Paginating our posts and breaking them into different pages and sections so we dont have too many at once. So we can set it to 5 post per page
    paginate_by = 5
    #Getting posts by a particuler user/username
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

#creating a view for individual posts.. we'll import DetailViews to look at the details of a single view, and add the path to our url
class PostDetailView(DetailView):
    model = Post


#users creating post from the page and we dont have to do it from the command line or the admin and add the path to our url
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
#overing the form valid method for create view so the author of the post is the current logged in user posting. Adding the author before the form is submitted
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#users updating post from the page and we dont have to do it from the command line or the admin. Add the path to our url
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
#overing the form valid method for create view so the author of the post is the current logged in user posting. Adding the author before the form is submitted
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#The UserPassesText would run this function to make sure that the user passes some text conditions before they can be allowed to update a post
    def test_func(self):
        post = self.get_object()
#To make sure that the current user is the author of the post
        if self.request.user == post.author:
            return True
        else:
            return False

#Our users been able to delete their posts. We take the arguments of LoginRequiredMixin, UserPassesTestMixin, on the left side of our DeleteView and add the path to our url
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
#After user deletes a post we want to send them to a success url, and here we are using/sending them back to homepage
    success_url = '/'
#The UserPassesText would run this function to make sure that the user passes some text conditions before they can be allowed to update a post
    def test_func(self):
        post = self.get_object()
#To make sure that the current user is the author of the post
        if self.request.user == post.author:
            return True
        else:
            return False

#adding the like button and like counter to our blog
@login_required
def like_post(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    like = Likes.objects.filter(Q(liked_by=user.id)&Q(post=post.id))
    if not like:
        post.number_of_likes += 1
        post.save()
        liked_post = Likes(post=post, liked_by=user.id)
        liked_post.save()
    #posts = Post.objects.all()
    return redirect('blog-home')
