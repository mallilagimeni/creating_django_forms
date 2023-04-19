from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[['PYTHON','python'],['JAVA','java'],['SQL','sql']]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    url=forms.URLField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    date=forms.DateTimeField()
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=g)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)