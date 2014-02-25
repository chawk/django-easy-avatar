.. django-easy-avatar documentation master file, created by
   sphinx-quickstart on Sun Feb 23 20:38:42 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-easy-avatar's documentation!
==============================================

A super easy AJAX loading avatar for profile management. **django-easy-avatar** is currently being used in production by Noob Media LLC for http://www.noobmovies.com

**django-easy-avatar** needs jQuery for ajax file uploading and validation. this plugin also uses Pillow for image manipulation and management.

Installation
------------
Install **django-easy-avatar** by running:

	``sudo easy_install django-easy-avatar``

Add to your installed apps within django settings.py file:

	``"easy_install"``

In that same settings.py file add:

	``FILE_SAVE_PATH = '/path/to/your/project/avatars'``

	``FILE_URL_PATH = 'http://your_website.com/location/to/avatars/'``

run syncdb command:

	``python manage.py syncdb``

important note!!, this must be added to your settings.py file:

	``TEMPLATE_CONTEXT_PROCESSORS = (``

	``'django.contrib.auth.context_processors.auth',``

	``'django.core.context_processors.debug',``

	``'django.core.context_processors.i18n',``

	``'django.core.context_processors.request',``

	``'django.core.context_processors.static',``

	``'django.contrib.messages.context_processors.messages',``

	``)``

By default, **django-easy-avatar** will overwrite the previous profile image for a particular user to save server hard disk space. If you wish to keep the image you can disable this feature by adding this to your settings.py file. 

	``OVERWRITE_PREVIOUS_FILES = False``

Add this line to your projects urls.py file. 

	``(r'^avatar/', include('easy_avatar.urls')),``

Adding **django-easy-avatar** to your templates
-------------------------------------------

Make sure you have included the **jQuery** library in your template by adding this to your html <head>:

	``<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>``

To add **django-easy-avatar** you simply have to add this to the top of your template: 
	
	``{% load avatar_tags %}``

Then, whereever you want the avatar image/form to appear you just add:

	``{% upload_form %}``

That's it! 

Video Tutorials
---------------

To see **django-easy-avatar** in action you can visit http://www.noobmovies.com and register your profile or you can watch a video tutorial located at http://www.youtube.com/watch?v=y1ndWIdK9WI

Additional tutorials will be coming soon regarding how you can style your form elements (for those who are not as familiar with CSS and JavaScript).  

Things to Consider
------------------

**django-easy-avatar** is geared towards more modern browsers.  Because it uses HTML5 and AJAX for file uploading, it may not work in older browsers such as Internet Explorer 9 and below.  

Contribute
----------
- Issue Tracker: https://github.com/chawk/django-easy-avatar/issues
- Source Code: This plugin is free to be adapted at GitHub; https://github.com/chawk/django-easy-avatar

Support
-------

**django-easy-avatar** was created by Chris Hawkes who is a web developer and programmer in Python, C# and JavaScript.  You can contact Chris Hawkes via github with questions or concerns.  https://github.com/chawk

License
-------
django-easy-avatar is free for commercial and non-commercial use under an MIT License.
