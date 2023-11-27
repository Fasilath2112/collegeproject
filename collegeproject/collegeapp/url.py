from collegeapp import admin, views
from django.urls import include, path

urlpatterns = [
    path('display/',views.display,name="display"),
    path('status/',views.status,name="status"),
    path('update/<int:pk>/',views.update,name="update"),
    path('delete/<int:pk>/',views.delete,name="delete"),
]