"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from app.views import auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(([
        path('params', auth_views.AuthParamsView.as_view()),
        path('sign_in', auth_views.SignInView.as_view()),
        # path('', auth_views.QuizListView.as_view()),
        
    ], 'auth'), namespace='auth')),
    
]


# config/routes.rb

"""
post "delete_account" => "admin#delete_account"
# extension settngs
get "extension-settings/:id/mute" => "extension_settings#mute"

# forward non-namespaced routes to api namespace
get 'auth/params' => "api/auth#auth_params"
post "auth/sign_in" => "api/auth#sign_in"
post "auth" => "api/auth#register"
post "auth/update" => "api/auth#update"
post "auth/change_pw" => "api/auth#change_pw"

post "items/sync" => "api/items#sync"
post "items/backup" => "api/items#backup"

delete "items" => "api/items#destroy"
resources "items", :controller => "api/items"
"""
