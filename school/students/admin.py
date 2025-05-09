from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'age', 'interest', 'course')
    search_fields = ('first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'age', 'interest', 'course')
    list_filter = [ 'date_of_birth', 'gender', 'age', 'interest', 'course']