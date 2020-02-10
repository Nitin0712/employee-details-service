from django.conf.urls import url
from django.urls import path, include
from restapp.views import *
from rest_framework import routers

route = routers.DefaultRouter()
route.register('',employeeList)

urlpatterns = [
    path('employee/', include(route.urls)),
    # path('<int:id>', employeeDetail.as_view(), name='employeeDetail')
]