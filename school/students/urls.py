

from django.urls import path
from .views import student_list, student_create, student_update, student_delete, predict_course

urlpatterns = [
    path('', student_list, name='student_list'),
    path('new/', student_create, name='student_create'),  # ✅ This must be BEFORE <int:pk> patterns!
    path('<int:pk>/edit/', student_update, name='student_update'),
    path('<int:pk>/delete/', student_delete, name='student_delete'),
    path('predict/',predict_course, name='predict_course'),  # ✅ This must be AFTER <int:pk> patterns!
]


