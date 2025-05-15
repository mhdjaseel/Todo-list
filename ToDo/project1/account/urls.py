from django.urls import path
from .import views
urlpatterns = [
path("signup/",views.signup, name="signup"),
path("",views.signin, name="signin"),
path("user_logout/",views.user_logout, name="user_logout")

]