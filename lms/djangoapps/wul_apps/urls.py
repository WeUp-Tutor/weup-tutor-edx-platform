from django.urls import path
from lms.djangoapps.wul_apps import views

urlpatterns = [
    path('', views.wul_apps_dummyview, name='testme_view'),
]
