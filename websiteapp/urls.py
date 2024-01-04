from django.urls import path,include
from .import views
urlpatterns = [
     path('',views.home,name="home"),
     path('loginpage',views.loginpage,name="loginpage"),
     path('signup',views.signup,name="signup"),
     path('about',views.about,name="about"),

     path('adduser',views.adduser,name="adduser"),
     path('login1',views.login1,name="login1"),
     path('logout/',views.logout,name="logout"),

]
      