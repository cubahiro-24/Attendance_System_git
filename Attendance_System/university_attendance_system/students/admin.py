from django.contrib import admin
from .models import Student

@admin.register(Student)  # Registering the Student model with the admin interface
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'birthdate')  # Updated field names
    search_fields = ('first_name', 'last_name', 'email')  # Updated search fields
