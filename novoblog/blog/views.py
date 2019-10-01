from django.shortcuts import render
from blog.forms import FormPost

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def create_post(request):
   form =  FormPost()
   return render(request,"blog/create_post.html",{"form":form})