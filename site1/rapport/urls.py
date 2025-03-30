from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('presentation/', views.presentation, name="presentation"),
    path('deroulement/', views.deroulement, name="deroulement"),
    path('describe/', views.description, name="describe"),
    path('conditions/', views.conditions, name="conditions"),
    path('remerciments/', views.merci, name="merci"),
    path('conclusion/', views.conclusion, name="conclusion"),
    path('docs/typescript/', views.typescript_doc, name='typescript_doc'),
    path('docs/mysql/', views.mysqldoc, name='mysql_doc'),
    path('docs/html/', views.htmldoc, name='htmldoc'),
    path('docs/doccss/', views.cssdoc, name='css-doc'),
    path('docs/php/', views.phpdoc, name='php-doc'),
    path('docs/debian/', views.debaindoc, name='debian-doc'),
    path('docs/glpi/', views.glpidoc, name='glpi-doc'),
    path('docs/axis/', views.axisdoc, name='axis-doc'),	
]