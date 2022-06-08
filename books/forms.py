from django.forms import ModelForm
from .models import Book

from django import forms

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        model._meta.get_field('email')._unique = True
        #fields = '__all__'
        fields  = ['first_name','last_name','email','username','password1','password2']
        #labels = {'first_name':'Name',}

        #widgets = {
        #    'tags': forms.CheckboxSelectMultiple(),
        #}

    def __init__(self, *args, **kwargs):

        super(CustomUserCreationForm,self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class': "form-control"})



class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('user','created')
        labels = {'Title':'Title','author':'Author',
        'publisher':'Publisher','sum_pages':'Pages'}
