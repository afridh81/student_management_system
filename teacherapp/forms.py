from core.models import  Profile,Allotted_Subject,Academic_year,Semester,Student,details
from django.forms import ModelForm
from django import forms


class AcademicForm(ModelForm):
    class Meta:
        model = Academic_year
        fields = ['academic']
class semesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = ['semester']

class ProfileUserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class Studdetails(ModelForm):
    class Meta:
        model=details
        fields=['student_name','Subject1','Internal','Assignment','attendence','assignment1']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'Registrations_No', 'Department', 'phone', 'semester']

class AllotedSubjectForm(forms.ModelForm):
    class Meta:
        model = Allotted_Subject
        fields = ['teacher','subject','department','semester','subject_code','academic']
class Text(forms.Form):
    TextField=forms.CharField(widget=forms.Textarea)


