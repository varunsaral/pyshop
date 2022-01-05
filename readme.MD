Learning django framework:

what is django framework ? 
Apart from the Google definition ,it's a python based framework for making websites

Steps in this project:

1) Installing the django , simply type <code>pip install django</code>
2) For init the project , type <code> django-admin startproject <project-name> </code>

Now to start development server:
    <code>python manage.py runserver</code>

We can debug and make our website through this dev server

Now we have to configure various pages and map the urls

For making the pages we have to use the views.py

The flow is : <br>
              1)make a view in views.py(make a function )</br>
              2) map a url with the function we made for that particular page in urls.py


We can isolate various functionality of the django app into modules and also can reuse them

For making a new module in the app we use <code>python manage.py startapp 'module name' </code>

Now for each module we can develop as different app , set the functionality in views and use url to bind the url

For example ,  we have to make a /new url in /production

we will define a function new in views and bind the url in urls

we also have to import the views module here to pass the reference of the func in list

In urls.py we have a list as url_patterns = [ 
            'address','function_name'
] 

For this app we made 

<code>
from django.urls import path<br>
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]
</code>
                
we also have to map the urls in main app in urlpatterns
For that include the production module there and use include() function 
In my case i imported that file as uls and gave that to include function()
It works not sure , it's the correct way

Also in views we make define function and write whatever it supposed to when someone hit that page

For example if someone hit /new , we will make function new

<code>def new(request):#request has all the data of request
    <br>return HttpResponse('new page')</code>

now we just have to pass this function reference in urls list with the url or our choice


Note : We are just using HttpResponse here for text based response

can be imported with <code>from django.http import HttpResponse</code>


Now for database we are using built in sqlite database , not suitable for production dataload

For that we can make a model in models.py and tell our django to generate the database through that model

In model.py we define a class with database name and also inherit the model class of django through models.Model

then we define the field

ex name = models.CharField(max_length="anynumber")

For applying that model we have to tell that in settings.py that we are using production model

In setting.py we have list of installed app there we have to type our production app config file which is <code>'production.apps.ProductionConfig'</code>

Now we have to give two commands <code>makemigrations and migrate</code>

and the database will form from the model 

