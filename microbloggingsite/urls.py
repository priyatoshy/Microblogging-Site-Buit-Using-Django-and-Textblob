
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


admin.site.site_header="Prasna"
admin.site.site_title="Keep Loring....."
admin.site.index_title="Prasna"
urlpatterns = [
    
    path('',include('blogs.urls')),
    path('users/',include('users.urls')),

    path('admin/', admin.site.urls),
    #path('users/',include('users.urls')),
     path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name="reset_password"),
    #"
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),
    #template_name="reset_password_sent.html"
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    #template_name="reset.html"
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name="password_reset_complete"),
    #template_name="reset_password_complete.html"
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


