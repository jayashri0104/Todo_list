from django.urls import path

from . views import list , Delete, Update

urlpatterns = [
     path("", list.as_view(), name="list"),
     path("delete/<int:pk>/", Delete.as_view(), name="task_delete"),
     path("update/<int:pk>/", Update.as_view(), name="task_update"),
]