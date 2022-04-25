from django.urls import path
from . import views



app_name = 'mlmodel'

urlpatterns = [
    path('predict/', views.predict_view , name='predict_view'),
    path('predict/result', views.result , name='result'),
    path('dashborad/', views.dashborad , name='dashborad'),
]
