from django.shortcuts import render

from django.shortcuts import render, render_to_response, HttpResponseRedirect
from models import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

def __get_user_authentication(request, user):
    '''
    Private method
    Check if user is authenticated
    :param request: django request
    :param user: user details from Post request
    :return: user object in auth_user table
    '''
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    return user

def __login_handler(request, user):
    '''
    Parse POST form and render required view
    :param request: django request
    :param user: auth_user table object
    :param is_submit: template variable indicating if avatar is submitted to remote machine
    :return: renders html template
    '''
    isAuthenticatedUser = __get_user_authentication(request, user)
    if isAuthenticatedUser and isAuthenticatedUser.is_superuser:
        login(request, isAuthenticatedUser)
        print "%s authenticated"%(isAuthenticatedUser.username)
    else:
        print "%s not authenticated"%(isAuthenticatedUser.username)
        return __render_mainpage(request)

def __render_mainpage(request):
    login_form = LoginForm()
    return render_to_response("mainpage/index.html",{"login_form": login_form},
                              context_instance=RequestContext(request))

@login_required()
def __render_managementpage(request):
        return render_to_response("management/index.html",context_instance=RequestContext(request))

def index(request):
    '''
    Display landing page if not login
    :param request: django request
    :return: renders html template
    '''
    user = request.user
    if request.POST:
        __login_handler(request, user)

    if not user.is_authenticated():
        #display login page
        return __render_mainpage(request)
    else:
        #display admin page
        return HttpResponseRedirect("management")