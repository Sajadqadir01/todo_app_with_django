from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='tasks'),
    path('task-update/<int:pk>', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', views.DeleteView.as_view(), name='delete-view')
]