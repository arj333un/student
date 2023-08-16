from django.urls import path
from .import views
urlpatterns = [
    
    path('',views.student,name='student'),
    path('register',views.register,name='register'),
    path('show_student_details',views.show_student_details,name='show_student_details'),
    path('editstd<int:pk>',views.editstd,name='editstd'),
    path('edit_student_details<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('show_student<int:pk>',views.show_student,name='show_student'),
    path('deletestd<int:pk>',views.deletestd,name='deletestd'),
    path('back',views.back,name='back'),
    
]