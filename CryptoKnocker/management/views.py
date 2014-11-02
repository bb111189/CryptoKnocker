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
    '''
    Overview of all the port status
    :param request:
    :return:
    '''
    portSet = __list_ports('userID','publicKey')
    just_logged_in = False
    #isFirstLogin = request.user.first_name
    isFirstLogin = False

    return render_to_response("management/index.html",{"portSet":portSet, "pageType":"overview", "just_logged_in":just_logged_in, "isFirstLogin":isFirstLogin},context_instance=RequestContext(request))

@login_required()
def user_login(request):
    '''
    Login page, display wizard if first time logged in, else display overview page
    :param request:
    :return:
    '''
    #isFirstLogin = request.user.first_name
    isFirstLogin = False
    portSet = __list_ports('userID','publicKey')
    just_logged_in = True

    return render_to_response("management/index.html",{"portSet":portSet, "pageType":"overview", "just_logged_in":just_logged_in, "isFirstLogin":isFirstLogin},context_instance=RequestContext(request))



@login_required()
def user_logout(request):
    '''
    Method for user logout
    :param request:
    :return:
    '''
    logout(request)
    return HttpResponseRedirect('/')

@login_required()
def registration(request):
    '''
    View method for registration process.
    :param request:
    :return:
    '''
    if request.POST:
        user_form = portProfileList(request.POST, request.FILES)
        print request.FILES
        c = {}
        c.update(csrf(request))

        if user_form.is_valid():
            profile = __save_to_database(user_form)
            portSet = __list_ports()

            #generate QR CODE here

            return render_to_response("management/index.html",{"pageType":"qrcode"},context_instance=RequestContext(request))
        else:
            return render_to_response("management/index.html",{"pageType":"registration", "user_form":user_form},context_instance=RequestContext(request))
    user_form = portProfileList()
    return render_to_response("management/index.html",{"pageType":"registration", "user_form":user_form},context_instance=RequestContext(request))

@login_required()
def manageKeys(request):
    if request.POST:
        c = {}
        c.update(csrf(request))
        id_value =  request.POST['form_id']
        profile = portProfile.objects.filter(id=id_value).delete()
        return HttpResponseRedirect("/management/keys/")

    portSet = __list_ports()
    return render_to_response("management/index.html",{"portSet":portSet, "pageType":"manageKeys"},context_instance=RequestContext(request))


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

def __list_ports(*exclusion):
    '''
    Private method
    Get all objects from management.portProfile table
    :return: port objects or False if no object found
    '''
    profile_formset = modelformset_factory(
        portProfile,
        exclude=(exclusion),
        labels=portProfileList.Meta.labels
    )

    portSet = profile_formset(queryset=portProfile.objects.all())
    if len(portSet) == 1:
        return False
    else:
        portSet = portSet[:-1] #remove last result which is None. (A problem with django)
        return portSet
