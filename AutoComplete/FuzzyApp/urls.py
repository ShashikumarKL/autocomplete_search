# filename: AutoComplete/FuzzyApp/urls.py

from django.conf.urls import url
from django.contrib import admin
import include
from . import views


urlpatterns = [
    url(r'^$',views.indexpage.as_view()),
    url(r'^display/',views.displaypage.as_view()),
   

]
