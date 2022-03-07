from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
  class Meta:
    model = Project
    exclude = ['vote_ratio', 'vote_total']
    widgets = {
      'tags': forms.CheckboxSelectMultiple()
    }

  def __init__(self, *args, **kwargs):
    super(ProjectForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})

    # Can edit each individual field
    # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
