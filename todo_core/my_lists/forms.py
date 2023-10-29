from django import forms
from .models import ToDoItem


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['name', 'description', 'is_completed', 'todo_list']
