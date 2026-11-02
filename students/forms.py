from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course', 'age', 'phone']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Student age must be atleast 18.")
        return age

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 10:
            raise forms.ValidationError("Phone number must be contain exactly 10 digits.")
        return phone

class StudentForms(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
    course = forms.CharField(max_length=100)