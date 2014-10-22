from django.shortcuts import render

from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from management.models import portProfileList, portProfile


# Create your views here.
@login_required()
def index(request):

    portSet = __list_ports()
    return render_to_response("management/index.html",{"portSet":portSet, "pageType":"overview"},context_instance=RequestContext(request))

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required()
def registration(request):
    '''if request.POST:
        user_form = portProfileList(request.POST)
        c = {}
        c.update(csrf(request))
        if user_form.is_valid():
            profile = __save_to_database(user_form)
            request.session["id"] = str(profile.user_id)
            portSet = __list_ports()
            return render_to_response("management/index.html",{"portSet":portSet, "pageType":"overview"},context_instance=RequestContext(request))
    '''
    user_form = portProfileList()
    return render_to_response("management/index.html",{"pageType":"registration", "user_form":user_form},context_instance=RequestContext(request))

def __save_to_database(user_form):
    '''
    Private method
    Save user details to database.
    :param profile_form: table object
    :return: table object
    '''
    profile = user_form.save()
    profile.save()
    return profile

def __list_ports():
    '''
    Private method
    Get all objects from management.portProfile table
    :return: port objects or False if no object found
    '''
    profile_formset = modelformset_factory(
        portProfile,
        exclude=('user',),
        labels=portProfileList.Meta.labels
    )

    portSet = profile_formset(queryset=portProfile.objects.all())
    if len(portSet) == 1:
        return False
    else:
        portSet = portSet[:-1] #remove last result which is None. (A problem with django)
        return portSet
