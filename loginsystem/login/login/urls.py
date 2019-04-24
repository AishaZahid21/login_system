# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from django.views.generic.base import TemplateView
# urlpatterns = [
#     path('', include('core.urls')),
#     path('accounts/home',
#          TemplateView.as_view(template_name='accounts/home.html'), name='home'),
#     # path('login', auth_views.LoginView.as_view(
#     #     template_name='registration/login.html'), name='login'),
#     # path('logout', auth_views.LogoutView.as_view(
#     #     template_name='registration/logout.html'), name='logout'),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('admin/', admin.site.urls),

# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
