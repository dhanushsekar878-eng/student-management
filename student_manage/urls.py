from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]


path('set-cookie/', views.set_cookie, name='set_cookie'),
path('get-cookie/', views.get_cookie, name='get_cookie'),
path('delete-cookie/', views.delete_cookie, name='delete_cookie'),




path('set-session/', views.set_session, name='set_session'),
path('get-session/', views.get_session, name='get_session'),
path('delete-session/', views.delete_session, name='delete_session'),