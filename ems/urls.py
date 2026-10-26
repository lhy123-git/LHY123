from django.contrib import admin
from django.urls import path
from app01.views import (
    dept_list, dept_add, dept_del, dept_edit,
    user_list, user_add, user_edit,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dept/', dept_list),
    path('dept/add/', dept_add),
    path('dept/del/<int:did>/', dept_del),
    path('dept/edit/<int:did>/', dept_edit),
    path('user/list/', user_list),
    path('user/add/', user_add),
    path('user/edit/<int:nid>/', user_edit),
]
