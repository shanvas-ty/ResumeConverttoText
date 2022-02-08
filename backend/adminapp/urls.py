
from adminapp import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('user', views.userlist, name="usr"),
    path('user/interviewer', views.interviewerslist, name="interview"),
    path('user/Candidates', views.Candidatelist, name="candi"),
    path('user/Company', views.CompanyList, name="comp"),
    path('user/Institute', views.InstituteList, name="inst"),
    path('user/QAuthor', views.QAuthorList, name="QA"),
  #  path('user/Profile', views.Profile, name="prof"),
    path('user/Profile/<str:userid>', views.Profile, name="prof"),
]