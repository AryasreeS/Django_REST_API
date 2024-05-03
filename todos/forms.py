from django import forms
#creates a form
#like class 
class todo_forms(forms.Form):
    content=forms.CharField(label='Todo content',max_length=100)
    
