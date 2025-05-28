from django import forms
from . import models

class  TodoForm(forms.ModelForm):
    class Meta:
        model = models.TodoModel
        exclude = ['user']
        # fields = '__all__'