"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from polls.views import *
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path("polls/", include("polls.urls")),
    path('',index,name="polls"),
    path('success_page/',success_page,name="success_page"),
    path('delete_receipe/<id>/',delete_receipe,name="delete_receipe"),
    path('update_receipes/<id>/',update_receipes,name="update_receipes"),
    path('login_page/',login_page,name="login_page"),
    path('logout_page/',logout_page,name="logout_page"),
    
    path('registration_page/',registration_page,name="registration_page"),
    path('receipes/',receipes,name="receipes"),
    path('about/', about, name="about"),
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


