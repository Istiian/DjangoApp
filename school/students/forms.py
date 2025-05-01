from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ['first_name', 'last_name', 'email', 'age', 'date_of_birth', 'gender', 'interests','course']
        fields = '__all__'
        
        widgets = {
            'interests': forms.CheckboxSelectMultiple,
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
    

    def __init__(self, *args, **kwargs):
            super(StudentForm, self).__init__(*args, **kwargs)
            # Format the initial value for the date field
            if self.instance and self.instance.date_of_birth:
                self.fields['date_of_birth'].initial = self.instance.date_of_birth.strftime('%Y-%m-%d')