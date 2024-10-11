from django.urls import path
from . import views
from .views import success_view, student_form, delete_student, modify_student, course_form, attendance_per_student, login_view, logout_view, home_view

urlpatterns = [
    path('student-form/', views.student_form, name='student_form'),
    path('success_student/', success_view, name='success_student_url'),  # Add this line
    path('students/delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('modify_student/<int:student_id>/', modify_student, name='modify_student'),

    path('lecturer-form/', views.lecturer_form, name='lecturer_form'),
    path('success_lecturer/', views.success_lecturer_view, name='success_lecturer_url'),
    path('lecturers/delete_lecturer/<int:lecturer_id>/', views.delete_lecturer, name='delete_lecturer'),
    path('modify_lecturer/<int:lecturer_id>/', views.modify_lecturer, name='modify_lecturer'),

    path('course-form/', views.course_form, name='course_form'),
    path('success_course/', views.success_course_view, name='success_course_url'),  # Add this line
    path('courses/delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('modify_course/<int:course_id>/', views.modify_course, name='modify_course'),

    path('admin-form/', views.admin_form_view, name='admin_form'),
    path('success_admin/', views.success_admin_view, name='success_admin'),
    path('admin/modify/<int:id>/', views.modify_admin_view, name='modify_admin'),
    path('admin/delete/<int:id>/', views.delete_admin_view, name='delete_admin'),

    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.add_attendance, name='add_attendance'),
    path('attendance/modify/<int:attendance_id>/', views.modify_attendance, name='modify_attendance'),
    path('attendance/delete/<int:attendance_id>/', views.delete_attendance, name='delete_attendance'),

    path('attendance/per-student/', attendance_per_student, name='attendance_per_student'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
]
