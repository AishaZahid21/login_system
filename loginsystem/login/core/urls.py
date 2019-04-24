from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    path('accounts/home',
         TemplateView.as_view(template_name='accounts/home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup, name='signup'),

]
