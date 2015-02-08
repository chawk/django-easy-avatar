django-easy-avatar
==================
        
A super easy AJAX loading avatar for profile management.  django-easy-avatar is currently being used in production by Noob Media LLC for http://www.noobmovies.com

Example...
http://www.findgamersonline.com/user/profile/1/

django-easy-avatar uses jQuery for ajax file uploading and validation.  this plugin also uses Pillow for image manipulation to resize images @ 100px X 100px while maintaining the correct aspect ratio.  It also uses standard HTML5 uploading progress to display uploading status.

If you need to override the custom styling of the Avatar upload buttons or image etc... just use CSS.  

If you feel this plugin needs additional features feel free to contact me with your suggestions or fork the project. 

== Installation Instructions ==

1.  pip install django-easy-avatar

2.  add easy_avatar to your installed apps

3.  add the below paths to your settings.py file (make sure you point to the right locations 

(example)

FILE_SAVE_PATH = "/root/path/to/your/static/avatars" ## must give apache or whatever webserver you're using write access to this directory

FILE_URL_PATH = "http://www.noobmovies.com/static/avatars/" ## your url where the uploaded image can be handled by your server

4.  Add 'django.core.context_processors.request' to your TEMPLATE_CONTEXT_PROCESSORS in your settings.py file. 
(example) 
TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'django.core.context_processors.request',
    ...
    )

5.  add (r'^avatar/', include('easy_avatar.urls')), to your urls.py file

6.  in the template where you plan on using django-easy-avatar add {% load avatar_tags %} to the top of the template, also add jQuery library. 

7.  to place the form in the page add the below
(example)
{% if request.user.is_authenticated and request.user.id == userProfile.user.id %}
        {% upload_form %}
{% else %}
        {{ avatar.image_url }}  /* wrap this in an image tag */
{% endif %}

If you have any troubles with this setup you will most likely be running into a permissions problem when your app tries to write the file to the directory.  

see this link for setting permissions to allow apache to create directories and files. 

http://askubuntu.com/questions/30629/how-can-i-recursively-change-the-permissions-of-files-and-directories



**** there is a known problem with trying to add an easy_avatar via the admin console, I will be looking into this ****
