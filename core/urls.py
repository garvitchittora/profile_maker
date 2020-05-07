from .views import main,display
from django.urls import path

urlpatterns = [
    path('',main),
    # path('', views.main,name = 'main'),
    path('display/',display)
]

