from django.db import models
from django.forms import ModelForm
from django import forms
from django.forms.models import BaseModelFormSet
from django.contrib.auth.models import User
from samba.web_server import render_placeholder


class LoginForm(ModelForm):
    '''
    Customization of login form
    '''
    class Meta:
        model = User
        fields = {'username', 'password'}
        labels = {
        'username' : 'Username',
        'password' : 'Password',

        }

        def custom_field_attr(placeholder="", classname="", focus=False):
            '''
            Method to create bootstrap css fields
            :param placeholder: text for input field's place holder
            '''
            attr = {
            'class':"form-control input-md " + classname,
            'id' : classname,
            'name' : classname,
            'required': "",
            'placeholder':placeholder,
            }

            if focus is True:
                attr['autofocus'] = ""

            return attr

        widgets = {
        'username' : forms.TextInput(attrs=custom_field_attr(placeholder="Enter Username", classname='username')),
        'password' : forms.PasswordInput(attrs=custom_field_attr(placeholder="Enter Password",classname='password'))
        }
        help_texts = {
        'username' : "",
        'password' : ""
        }

