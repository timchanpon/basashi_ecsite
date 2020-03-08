from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('part_name', 'details', 'num_grams', 'purchase_amt')
