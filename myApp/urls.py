from django.urls import path
from . import views

urlpatterns = [
    # 路由匹配
    path('get_student_list', views.get_student_list, name='get_student_list'),
    path('add_student', views.add_student),
]
