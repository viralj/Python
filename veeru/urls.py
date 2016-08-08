"""veeru URL Configuration
    
    The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
    Examples:
    Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
    Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
    Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    """
from django.conf.urls import url, include

# from django.contrib import admin
from veeru.AboutBTTGame import AboutBTTGame
from veeru.HomePage import HomePage
from veeru.TestConnection import TestConnection

urlpatterns = [
               # url(r'^admin/', admin.site.urls),
               
               url(r'^webapi/', include('useraccess.urls')),
               url(r'^webapi/TestConnection$', TestConnection.as_view(), name="Test mobile connection"),
               url(r'^webapi/game/BTT/', include('btt.urls')),
               
               url(r'^BTT/About$', AboutBTTGame.as_view(), name="About BitTacToe Game"),
               url(r'^$', HomePage.as_view(), name="Home Page"),
               
               
               ]
