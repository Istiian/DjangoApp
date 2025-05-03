from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import joblib
import os
from django.conf import settings
import traceback
import pandas as pd
from django.contrib import messages 


gender_encoder = joblib.load(os.path.join(settings.BASE_DIR, 'school', 'AI_models', 'gender_encoder.joblib'))
program_encoder = joblib.load(os.path.join(settings.BASE_DIR, 'school', 'AI_models', 'program_encoder.joblib'))
mlb = joblib.load(os.path.join(settings.BASE_DIR, 'school', 'AI_models', 'multilabel_binarizer.joblib'))
model = joblib.load(os.path.join(settings.BASE_DIR, 'school', 'AI_models', 'predict_course.joblib'))


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Student Created Successfully!") 
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Student Information is Successfully Updated!") 
        return redirect('student_list')

    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)  # ✅ Ensure this only works with valid pk
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student Deleted Successfully!") 
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})


@csrf_exempt
def predict_course(request, pk=None):
    if request.method == 'POST':
        try:
            age = request.POST.get("age")
            interest = request.POST.get("interests")
            gender = request.POST.get("gender")

            interest_list = interest.split(',')

            # Encode inputs
            gender_encoded = gender_encoder.transform([gender])[0]
            interests_encoded = mlb.transform([interest_list])[0]

            # Construct feature vector and DataFrame
            features = [int(age), gender_encoded] + list(interests_encoded)
            feature_names = ['Age', 'Gender'] + list(mlb.classes_)
            sample_df = pd.DataFrame([features], columns=feature_names)

            # Predict
            prediction = model.predict(sample_df)
            course = program_encoder.inverse_transform(prediction)[0]

            print("Predicted course:", course)
            return JsonResponse({"course": course})
        
        except Exception as e:
            print("❌ Error occurred in predict_course:")
            traceback.print_exc()
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)



    