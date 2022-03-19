

from django.urls import path, include

from .views import TaskList, TaskDetails


urlpatterns = [
    path('<int:pk>/', TaskDetails.as_view()),
    path('', TaskList.as_view()),
]
