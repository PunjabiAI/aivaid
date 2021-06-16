
from django import forms

from superuser.models import blog,categories


class blogForm(forms.ModelForm):
    title = forms.CharField(required=False, max_length=2000)
    # categoblogries = forms.CharField(required=False, max_length=2000)
    image = forms.ImageField(max_length=2000,required=False)
    description = forms.CharField(max_length=50000,required=False)
    meta_title = forms.CharField(max_length=2000,required=False)
    meta_keyword = forms.CharField(max_length=2000,required=False)
    meta_description = forms.CharField(max_length=2000,required=False)
    class Meta:
        model = blog
        fields = ['title','image', 'description', 'meta_title', 'meta_keyword', 'meta_description',]

class blogseditForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title','image','description', 'meta_title', 'meta_keyword', 'meta_description',]

class categoriesForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=1000)
    description = forms.CharField(max_length=10000)
    # meta_title = forms.CharField(max_length=1000)
    # meta_keyword = forms.CharField(max_length=1000)
    # meta_description = forms.CharField(max_length=1000)

    class Meta:
        model = categories
        fields = ['name', 'description']


class categorieseditForm(forms.ModelForm):

    class Meta:
        model = categories
        fields = ['name', 'description']
