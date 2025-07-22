from django.urls import path

from . views import listView , DeleteView, UpdateView

urlpatterns = [
     path("", listView.as_view(), name="list"),
     path("delete/<int:pk>/", DeleteView.as_view(), name="task_delete"),
     path("update/<int:pk>/", UpdateView.as_view(), name="task_update"),
]