from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class portProfile(models.Model):
    '''
    Table for portProfile. Add columns if required here.
    '''
    user = models.OneToOneField(User)

    name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=100 , blank=False, default="")
    password = models.CharField(max_length=100 , blank=False, default="")


    def __unicode__(self):
        return self.user.username

class portProfileList(ModelForm):
    class Meta:
        '''
        Display port profile list
        '''
        model = portProfile

        #fields order determines html form order
        fields =('name', 'username', 'password', 'password')
        labels = {
            'name' : 'Name',
            'username' : 'Username',
            'password' : 'Password',
            }

        def custom_field_attr(classname="", placeholder="none"):
            '''
            Method to create bootstrap css fields
            :param placeholder: text for input field's place holder
            :return: nil
            '''
            attr = {
                'class':"form-control input-md " + classname,
                'required': "",
                'placeholder':placeholder,
                }
            return attr

        widgets = {
            'name' : forms.TextInput(attrs=custom_field_attr('name', "Enter your name")),
            'username' : forms.TextInput(attrs=custom_field_attr('username', "Enter Username")),
			'password' : forms.PasswordInput(attrs=custom_field_attr('password', "Enter Password")),
        }

        help_texts = {

        }

        error_messages = {

        }