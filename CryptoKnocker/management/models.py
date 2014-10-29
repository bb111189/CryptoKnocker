from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

class portProfile(models.Model):
    '''
    Table for portProfile. Add columns if required here.
    '''
    userID = models.CharField(max_length=50, blank=False)
    port = models.PositiveIntegerField(max_length=5, blank=False)
    serviceName = models.CharField(max_length="20", blank=False)
    publicKey = models.FileField(blank=False, upload_to="./publickeys/")

    class Meta:
        unique_together = ("userID", "port")

    def __unicode__(self):
        return self.user.username

class portProfileList(ModelForm):
    class Meta:
        '''
        Display port profile list
        '''
        model = portProfile

        #fields order determines html form order
        fields =('userID', 'port', 'serviceName', 'publicKey')
        labels = {
            'userID' : 'User ID',
            'port' : 'Port',
            'serviceName' : 'Service Name',
            'publicKey' : 'Public Key',
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
            'userID' : forms.TextInput(attrs=custom_field_attr('userID', "Enter user ID")),
            'port' : forms.NumberInput(attrs=custom_field_attr('port', "Enter port")),
			'serviceName' : forms.TextInput(attrs=custom_field_attr('serviceName', "Enter service name")),
			'publicKey' : forms.ClearableFileInput(attrs=custom_field_attr('publicKey')),
        }

        help_texts = {

        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
                }
        }
