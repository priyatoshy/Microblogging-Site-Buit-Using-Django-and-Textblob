from django.urls import path 
from . import views
#imporing path 
#import views file from its own directory

#creating an url configuration/URLConf


urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('newblog',views.newblog,name='newblog'),
    #path('newblog',views.analysis,name='newblog'),
    
    path('blog/<str:pk>',views.showblog,name='show'),
    #note:-the named url just points to 
    #the non variable part 
    #and gets combined with the variable part
    path('rate1/<str:pk>',views.rate1,name='rate1'),
    path('rate2/<str:pk>',views.rate2,name='rate2'),
    path('rate3/<str:pk>',views.rate3,name='rate3'),
    path('report/<str:pk>',views.report,name='report'),
    path('comment/<str:pk>',views.comment,name='comment'),
    path('update/<str:pk>',views.updateblog,name='update'),
    #path('update/<str:pk>',views.analysis,name='update'),
    path('delete/<str:pk>',views.deleteblog,name='delete')
    #<a href="{% 'show' data.id %}">View</a>
    #the url above will take a contain the primary key of the blog
    #which will sent to a particular view function
    #the function will access and use it to  fetch data
    #path('blogs',views.blogs,name='blogs'),
]

