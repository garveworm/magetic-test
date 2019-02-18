from django.urls import path

from . import views


urlpatterns = [
    path('api/', views.ResultAPIView.as_view(), name='ResultAPIView'),
    path('html/', views.ResultHTMLView, name='ResultHTMLView'),
]
