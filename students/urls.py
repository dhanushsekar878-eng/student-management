from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_student, name='home'),  
    path('student_list/', views.student_list, name='student_list'),
    path('student_details/', views.student_details, name='student_details'),
    path('student_course/', views.student_course, name='student_course'),
    path('create/', views.create_student, name='create_student'),
    path('student_form/', views.student_form, name='student_form'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]

path('set-cookie/', views.set_cookie,name='set_cookie'),
path('get-cookie/', views.get_cookie,name='get_cookie'),
path('delete-cookie/', view.delete_cookie,name='delete_cookie'),