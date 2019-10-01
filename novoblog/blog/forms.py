from django.forms import ModelForm
from blog.models import Post

class FormPost(ModelForm):
    class Meta:
        model = Post 
        fields="__all__"
   