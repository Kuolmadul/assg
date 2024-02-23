from . import views
from django.urls import path
from django.urls.conf import path


urlpatterns = {
    path('', views.index),
    path('portfolio/', views.portfolio),
    path('page/', views.inner),

}