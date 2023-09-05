from django import forms
from .models import Notes, Homework, Todo


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }

class DateInput(forms.DateTimeInput):
    input_type = 'date'
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        # fields = '__all__'
        fields = ['subject','title','description','due','is_complete']
        widgets = {
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'due': DateInput(),
            # 'is_complete': forms.Bool(attrs={'class':'form-control'}),
        }

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100,required=True)

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields  = ['title','is_finished']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'})
        }