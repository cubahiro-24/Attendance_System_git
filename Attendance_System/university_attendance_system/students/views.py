# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, LecturerForm,CourseForm, AdminForm, AttendanceForm
from .models import Student, Lecturer, Course, Admin, Attendance  # Import your model here
from django.db.models import Q  # Import Q for complex queries
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_student_url')  # Ensure this matches the name in urls.py
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def success_view(request):
    # You can modify this to display the latest submitted student or all students
    students = Student.objects.all()  # Get all students
    return render(request, 'students/success.html', {'students': students})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('success_student_url')  # Redirect to the success page or wherever you wan

def modify_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect after successful modification
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/modify_student.html', {'form': form})


# Create a new lecturer
def lecturer_form(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_lecturer_url')  # Ensure this matches the name in urls.py
    else:
        form = LecturerForm()
    return render(request, 'students/lecturer_form.html', {'form': form})

def success_lecturer_view(request):
    lecturers = Lecturer.objects.all()  # Get all lecturers
    return render(request, 'students/success_lecturer.html', {'lecturers': lecturers})

def delete_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)
    if request.method == 'POST':
        lecturer.delete()
        return redirect('success_lecturer_url')  # Redirect to the success page

def modify_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('success_lecturer_url')  # Redirect after modification
    else:
        form = LecturerForm(instance=lecturer)

    return render(request, 'lecturer/modify_lecturer.html', {'form': form})


def course_form(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_course_url')  # Redirect to the success page
    else:
        form = CourseForm()

    lecturers = Lecturer.objects.all()  # Get all lecturers from the database
    return render(request, 'students/course_form.html', {'form': form, 'lecturers': lecturers})

def success_course_view(request):
    courses = Course.objects.all()  # Get all courses
    return render(request, 'students/success_course.html', {'courses': courses})

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('success_course_url')  # Redirect to the success page

def modify_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('success_course_url')  # Redirect after successful modification
    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/modify_course.html', {'form': form})


def admin_form_view(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_admin')
    else:
        form = AdminForm()
    return render(request, 'students/admin_form.html', {'form': form})

def success_admin_view(request):
    admins = Admin.objects.all()
    return render(request, 'students/success_admin.html', {'admins': admins})

def modify_admin_view(request, id):
    admin = get_object_or_404(Admin, id=id)
    if request.method == 'POST':
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('success_admin')  # Adjust to your actual success URL
    else:
        form = AdminForm(instance=admin)
    return render(request, 'students/modify_admin.html', {'form': form})

def delete_admin_view(request, id):
    admin = get_object_or_404(Admin, id=id)
    if request.method == 'POST':
        admin.delete()
        return redirect('success_admin')  # redirect to success page
    return render(request, 'students/confirm_delete.html', {'admin': admin})


def attendance_list(request):
    attendances = Attendance.objects.all()  # Retrieve all attendance records
    return render(request, 'students/attendance_list.html', {'attendances': attendances})

def add_attendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_per_student')  # Adjust according to your URL pattern
    else:
        form = AttendanceForm()
    return render(request, 'students/add_attendance.html', {'form': form})

def modify_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_per_student')  # Adjust according to your URL pattern
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'students/modify_attendance.html', {'form': form})

def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == "POST":
        attendance.delete()
        return redirect('attendance_list')  # Adjust according to your URL pattern
    return render(request, 'students/delete_attendance.html', {'attendance': attendance})


def attendance_per_student(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    attendance_records = Attendance.objects.all()

    if request.method == "POST":
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course')
        date = request.POST.get('date')

        # Filter by student name or ID
        if student_name or student_id:
            filters = Q()
            if student_name:
                # Assuming your Student model has 'first_name' and 'last_name'
                filters |= Q(student__first_name__icontains=student_name) | Q(student__last_name__icontains=student_name)
            if student_id:
                filters |= Q(student__id=student_id)

            attendance_records = attendance_records.filter(filters)

        # Filter by course
        if course_id:
            attendance_records = attendance_records.filter(course_id=course_id)

        # Filter by date
        if date:
            attendance_records = attendance_records.filter(date=date)

    return render(request, 'students/attendance_per_student.html', {
        'students': students,
        'courses': courses,
        'attendance_records': attendance_records,
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change to your home page view
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Change to your login page view

@login_required
def home_view(request):
    return render(request, 'home.html')  # Change to your home page template


# Temporary in-memory storage for testing
students_data = [
    {"username": "student1", "password": "pass1"},
    {"username": "student2", "password": "pass2"},
    # Add more sample students as needed
]


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check against in-memory data
        user = next((student for student in students_data if
                     student['username'] == username and student['password'] == password), None)

        if user is not None:
            # Simulate login by storing username in session
            request.session['username'] = username
            return redirect('student_form')  # Redirect to student_form after login
        else:
            return render(request, 'students/login.html')

    return render(request, 'students/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # Change to your login page view

@login_required
def home_view(request):
    return render(request, 'home.html')  # Change to your home page template