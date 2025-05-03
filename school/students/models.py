from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)])
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]
    )
    interest = MultiSelectField(
        choices = [
            ('Accounting', 'Accounting'),
            ('Advertising', 'Advertising'),
            ('Branding', 'Branding'),
            ('Business', 'Business'),
            ('Business Strategy', 'Business Strategy'),
            ('Child Development', 'Child Development'),
            ('Coding', 'Coding'),
            ('Community Service', 'Community Service'),
            ('Consumer Behavior', 'Consumer Behavior'),
            ('Counseling', 'Counseling'),
            ('Debating', 'Debating'),
            ('Drawing', 'Drawing'),
            ('Economics', 'Economics'),
            ('Entrepreneurship', 'Entrepreneurship'),
            ('Finance', 'Finance'),
            ('Fitness', 'Fitness'),
            ('Gaming', 'Gaming'),
            ('Geography', 'Geography'),
            ('History', 'History'),
            ('Human Rights', 'Human Rights'),
            ('Investment', 'Investment'),
            ('Journalism', 'Journalism'),
            ('Law', 'Law'),
            ('Leadership', 'Leadership'),
            ('Math', 'Math'),
            ('Music', 'Music'),
            ('Negotiation', 'Negotiation'),
            ('Painting', 'Painting'),
            ('Philosophy', 'Philosophy'),
            ('Photography', 'Photography'),
            ('Politics', 'Politics'),
            ('Psychology', 'Psychology'),
            ('Reading', 'Reading'),
            ('Robotics', 'Robotics'),
            ('Social Justice', 'Social Justice'),
            ('Social Media', 'Social Media'),
            ('Social Skills', 'Social Skills'),
            ('Social Work', 'Social Work'),
            ('Statistics', 'Statistics'),
            ('Teaching', 'Teaching'),
            ('Technology', 'Technology'),
            ('Traveling', 'Traveling'),
            ('Writing', 'Writing')
        ],
        max_choices=3, 
        blank=False,     
        null=True,
        help_text="Select up to 3 interests.", 
    )

    course = models.CharField(
        choices=[
            ('Criminology', 'Criminology'),
            ('Information technology', 'Information technology'),
            ('Accountancy', 'Accountancy'),
            ('Early Childhood Education', 'Early Childhood Education'),
            ('Journalism', 'Journalism'),
            ('Elementary Education', 'Elementary Education'),
            ('Secondary Education Major in English', 'Secondary Education Major in English'),
            ('Secondary Education Major in Mathematics', 'Secondary Education Major in Mathematics'),
            ('Secondary Education Major in Social Studies', 'Secondary Education Major in Social Studies'),
            ('Political Science', 'Political Science'),
            ('Public Administration', 'Public Administration'),
            ('Social Work', 'Social Work'),
            ('Business Administration Major in Financial Management', 'Business Administration Major in Financial Management'),
            ('Business Administration Major in Human Resource Management', 'Business Administration Major in Human Resource Management'),
            ('Business Administration Major in Marketing Management', 'Business Administration Major in Marketing Management'),
            ('Management Accounting', 'Management Accounting')
        ],
        max_length=100,
        blank=False,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"