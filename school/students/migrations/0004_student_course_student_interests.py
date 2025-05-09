# Generated by Django 5.1.6 on 2025-04-29 11:51

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('Accounting', 'Accounting'), ('Advertising', 'Advertising'), ('Branding', 'Branding'), ('Business', 'Business'), ('Business Strategy', 'Business Strategy'), ('Child Development', 'Child Development'), ('Coding', 'Coding'), ('Community Service', 'Community Service'), ('Consumer Behavior', 'Consumer Behavior'), ('Counseling', 'Counseling'), ('Debating', 'Debating'), ('Drawing', 'Drawing'), ('Economics', 'Economics'), ('Entrepreneurship', 'Entrepreneurship'), ('Finance', 'Finance'), ('Fitness', 'Fitness'), ('Gaming', 'Gaming'), ('Geography', 'Geography'), ('History', 'History'), ('Human Rights', 'Human Rights'), ('Investment', 'Investment'), ('Journalism', 'Journalism'), ('Law', 'Law'), ('Leadership', 'Leadership'), ('Math', 'Math'), ('Music', 'Music'), ('Negotiation', 'Negotiation'), ('Painting', 'Painting'), ('Philosophy', 'Philosophy'), ('Photography', 'Photography'), ('Politics', 'Politics'), ('Psychology', 'Psychology'), ('Reading', 'Reading'), ('Robotics', 'Robotics'), ('Social Justice', 'Social Justice'), ('Social Media', 'Social Media'), ('Social Skills', 'Social Skills'), ('Social Work', 'Social Work'), ('Statistics', 'Statistics'), ('Teaching', 'Teaching'), ('Technology', 'Technology'), ('Traveling', 'Traveling'), ('Writing', 'Writing')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Criminology', 'Criminology'), ('Information technology', 'Information technology'), ('Accountancy', 'Accountancy'), ('Early Childhood Education', 'Early Childhood Education'), ('Journalism', 'Journalism'), ('Elementary Education', 'Elementary Education'), ('Secondary Education Major in English', 'Secondary Education Major in English'), ('Secondary Education Major in Mathematics', 'Secondary Education Major in Mathematics'), ('Secondary Education Major in Social Studies', 'Secondary Education Major in Social Studies'), ('Political Science', 'Political Science'), ('Public Administration', 'Public Administration'), ('Social Work', 'Social Work'), ('Business Administration Major in Financial Management', 'Business Administration Major in Financial Management'), ('Business Administration Major in Human Resource Management', 'Business Administration Major in Human Resource Management'), ('Business Administration Major in Marketing Management', 'Business Administration Major in Marketing Management'), ('Management Accounting', 'Management Accounting')], max_length=467, null=True),
        ),
    ]
