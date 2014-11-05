from django.shortcuts import render

from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from models import portProfileList, portProfile
<<<<<<< HEAD
from django.conf import settings
from os.path import join
from libs.crypto import generate_RSA
=======
from libs.pyg2fa import qrCodeURL, validate

>>>>>>> a88baecc939bfa8560ce7ce2c0b18a6663a5fe1f

# Create your views here.


@login_required()
def index(request):
    '''
    Overview of all the port status
    :param request:
    :return:
    '''
    portSet = __list_ports(False,'publicKey')
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
    portSet = __list_ports(False,'publicKey')
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
            #portSet = __list_ports(True)

            #generate QR CODE here
            randomSeed = "KKK67SDNLXIOG65U" #random 16 digit base 32 no # store this inside DB hardcode first
            QRCodeURL = qrCodeURL("CryptoKnocker", randomSeed) ## url for qr code. Basically user need to key in this rando

            return render_to_response("management/index.html",{"pageType":"qrcode", 'QRCodeURL': QRCodeURL},context_instance=RequestContext(request))
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

    portSet = __list_ports(True)
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

def __list_ports(everything,*exclusion):
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
    if everything:
        portSet = profile_formset(queryset=portProfile.objects.all())
    else:
        portSet = profile_formset(queryset=portProfile.objects.all().filter(status="open").order_by('-status'))

    if len(portSet) == 1:
        return False
    else:
        portSet = portSet[:-1] #remove last result which is None. (A problem with django)
        return portSet

@login_required()
def getPorts(request):
    portSet = __list_ports(False,'publicKey')

    return render_to_response("management/listPorts.html",{"portSet":portSet},context_instance=RequestContext(request))

@login_required()
def changeKey(request):
    keyPair = generate_RSA()
    privateKey = keyPair[0]
    publicKey = keyPair[1]

    file = open(join(settings.MEDIA_ROOT,"server_public.key"), "r+")
    file.writelines(publicKey)
    file.close()

    file2 = open(join(settings.MEDIA_ROOT,"server_private.key"), "r+")
    file2.writelines(privateKey)
    file2.close()

    return manageKeys(request)
