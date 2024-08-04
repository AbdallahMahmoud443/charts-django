from django.urls import path
from . import views

urlpatterns = [
    path('home',views.Home,name="HomePage"),
    path('get_chart_data/<str:chartType>/',views.Get_Chart_Data,name="get_chart_data")
]
