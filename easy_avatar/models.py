from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import os
from PIL import Image
import errno


def content_file_name(instance, filename):
    FILE_SAVE_PATH = getattr(settings, "FILE_SAVE_PATH", None)
    FILE_SAVE_PATH = FILE_SAVE_PATH + '/' + instance.user.username + '/'
    
    ## this determines whether user file already exist, if not it creates one. 
    try:
        os.makedirs(FILE_SAVE_PATH)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    FILE_SAVE_PATH = FILE_SAVE_PATH + filename

    return FILE_SAVE_PATH

class Easy_Avatar(models.Model):
    user = models.OneToOneField(User)
    docfile = models.FileField(upload_to=content_file_name)
    image_url = models.CharField(max_length=200, null=True, blank=True)