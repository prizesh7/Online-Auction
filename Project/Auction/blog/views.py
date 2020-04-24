from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from .filters import PostFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def home(request):
    
    posts = Post.objects.all()
    
    return render(request, 'blog/home.html', {'posts':posts})





class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'base_price', 'raising_price', 'product_category', 'date', 'hour', 'minite']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'base_price', 'raising_price', 'product_category', 'date', 'hour', 'minite']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(status="bidding")

class ElectronicListView(ListView):
    model = Post
    template_name = 'blog/electronic.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(status="bidding", product_category="electronic")

class ArtListView(ListView):
    model = Post
    template_name = 'blog/art.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(status="bidding", product_category="art")

class PropertiesListView(ListView):
    model = Post
    template_name = 'blog/properties.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(status="bidding", product_category="propertie")

def electronics(request):
    s = Post.objects.filter(product_category="electronic",status='bidding')
    return render(request, 'blog/electronic.html', {'s': s})

def art(request):
    s = Post.objects.filter(product_category="art",status='bidding')
    return render(request, 'blog/art.html', {'s': s})

def properties(request):
    s = Post.objects.filter(product_category="propertie",status='bidding')
    return render(request, 'blog/properties.html', {'s': s})

def details(request):
    s = Post.objects.get(id=request.GET['num1'])
    return render(request, 'blog/auction.html', {'s': s})


def auction(request):
    s = Post.objects.get(id=request.GET['num1'])
    if (request.GET['inc'] == 'yes'):
        if (s.sell_price == 0):
            s.sell_price = s.base_price
        else:
            s.sell_price = s.raising_price + s.sell_price
        s.status = 'bidding'
        # s.sell_price = 200 + s.sell_price
        s.sell_customer_name = request.user.username
        s.save()
        reload = 'yes'
    else:
        reload = 'no'
    return render(request, 'blog/auction.html', {'s': s, 'reload': reload})

def sold(request):
    s = Post.objects.get(id=request.GET['num1'])

    if(request.GET['do']=='yes'):
        if (s.status == 'bidding' and s.sell_price == 0 ):
            s.status = 'unsold'
        else:
            s.status = 'sold'
        s.save()
    else:
        return render(request, 'blog/auction.html', {'s': s, 'reload': 'no'})

    return render(request, 'blog/sold.html', {'s': s})

class MyItemListView(ListView):
    model = Post
    template_name = 'blog/myitem.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(sell_customer_name=self.request.user.username)

def myitem(request):
    s = Post.objects.filter(sell_customer_name=request.user.username)

    return render(request, 'blog/myitem.html', {'s': s})


class MyaddedListView(ListView):
    model = Post
    template_name = 'blog/myadded.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(author__username=self.request.user.username)

def myadded(request):
    s = Post.objects.filter(author__username=request.user.username)

    return render(request, 'blog/myadded.html', {'s': s})

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)

def history(request):
    s = Post.objects.filter(status="sold") | Post.objects.filter(status="unsold")

    return render(request, 'blog/history.html', {'s': s})

class PostFilterListView(ListView):
    model=Post
    template_name = 'blog/searchpost.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

