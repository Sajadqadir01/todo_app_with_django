from django.urls import path
from . import views
urlpatterns=[
    path('task-create', views.index, name='task-create'),
    path('', views.TaskList.as_view(), name='tasks'),
    path('task-update/<int:pk>', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', views.DeleteView.as_view(), name='delete-view')
]