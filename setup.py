import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-easy-avatar',
    version='0.1',
    packages=['easy_avatar'],
    include_package_data=True,
    zip_safe = False,
    license='MIT License',
    description='A super easy AJAX loading avatar for profile management.',
    long_description=README,
    url='http://www.noobmovies.com/',
    author='Chris Hawkes',
    author_email='noobniche@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)



