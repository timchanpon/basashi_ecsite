from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('part', 'details', 'image', 'price', 'num_grams', 'purchase_amt', 'exp_date', )
