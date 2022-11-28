from django.urls import path 
from . import views
#imporing path 
#import views file from its own directory

#creating an url configuration/URLConf


urlpatterns = [
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('register',views.registerUser,name='register'),
    path('profile',views.home,name='profile'),
    path('show-profile/<str:pk>',views.show_profile,name='show-profile'),
    path('update-profile/<str:pk>',views.update_profile,name='update-profile'),
    path('inbox/<str:pk>',views.inbox,name='inbox'),

]



    #path('log',views.login,name='log'),
    #<a href="{% 'show' data.id %}">View</a>
    #the url above will take a contain the primary key of the blog
    #which will sent to a particular view function
    #the function will access and use it to  fetch data
    #path('blogs',views.blogs,name='blogs'),