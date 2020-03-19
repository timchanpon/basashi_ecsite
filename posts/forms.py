from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('part_name', 'details', 'image', 'price', 'num_grams', 'purchase_amt', )
