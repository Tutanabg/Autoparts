from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("pay", views.pay, name="pay"),
    path("newparts", views.newparts, name="newparts"),
    path("parts/<str:item>/", views.parts, name="parts"),
    path("body/<str:item>/", views.body, name="body"),
    path("doors/<str:item>/", views.doors, name="doors"),
    path("avdevices/<str:item>/", views.avdevices, name="avdevices"),
    path("cameras/<str:item>/", views.cameras, name="cameras"),
    path("windows/<str:item>/", views.windows, name="windows"),
    path("newbody", views.newbody, name="newbody"),
    path("newdoor", views.newdoor, name="newdoor"),
    path("newav", views.newav, name="newav"),
    path("newcamera", views.newcamera, name="newcamera"),
    path("newwindow", views.newwindow, name="newwindow"),
    path("payment", views.payment, name="payment"),
    
    # API Routes
    path("bodyapi", views.bodyapi, name="bodyapi"),
    path("doorsapi", views.doorsapi, name="doorsapi"),
    path("avdevicesapi", views.avdevicesapi, name="avdevicesapi"),
    path("camerasapi", views.camerasapi, name="camerasapi"),
    path("windowsapi", views.windowsapi, name="windowsapi"),
]
