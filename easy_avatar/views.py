from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from easy_avatar.forms import UploadFileForm
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from django.conf import settings
from easy_avatar.models import Easy_Avatar
from django.http import HttpResponse
import os
import errno
from PIL import Image
import json


@requires_csrf_token
def upload(request):
    message = ""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return handle_uploaded_file(request, request.FILES['file'])
        else:
            form = UploadFileForm()
        return render(request, {'form': form, 'message':message})


def handle_uploaded_file(request, f):

    response = {}

    image = "" 

    FILE_URL_PATH = getattr(settings, "FILE_URL_PATH", None)

    FILE_SAVE_PATH = getattr(settings, "FILE_SAVE_PATH", None)
    if request.user.is_authenticated():
        user = request.user
    
    FILE_SAVE_PATH = FILE_SAVE_PATH + '/' +  user.username + '/'

    OVERWRITE_PREVIOUS_FILES = getattr(settings, "OVERWRITE_PREVIOUS_FILES", None)

    ## this determines whether user file already exist, if not it creates one.  If one exist it deletes what's there to replace
    try:
        os.makedirs(FILE_SAVE_PATH)
    except OSError as exception:
        ## true by default unless overridden by settings.py
        if OVERWRITE_PREVIOUS_FILES != False:
            for the_file in os.listdir(FILE_SAVE_PATH):
                file_path = os.path.join(FILE_SAVE_PATH, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    pass
        if exception.errno != errno.EEXIST:
            raise

    try:
        size = (100, 100)
        image = Image.open(f)
        image.thumbnail(size,Image.ANTIALIAS)
        image.save(FILE_SAVE_PATH + f.name, image.format)
        ## create the user avatar if one if not created
        insert = Easy_Avatar.objects.get_or_create(user=user)
        ## now that a user is created we can update it's avatar image location
        avatar = Easy_Avatar.objects.get(user=user)
        avatar.docfile = FILE_SAVE_PATH + f.name
        avatar.image_url = FILE_URL_PATH + user.username + '/' + f.name
        avatar.save()
        response["message"] = "Success"
        response["image_url"] = FILE_URL_PATH + user.username + '/' + f.name

    except: 
        response["message"] = "I'm sorry we could not upload your image"
        response["image_url"] = ""

    
    
    return HttpResponse(json.dumps(response), content_type="application/json")