from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = [ 'first_name', 'last_name', 'email', 'username', 'password1', 'password2']
    # labels = {
    #   'first_name': 'Name'
    # }

  def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    # Apply same attributes to all
    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})

    # Can edit each individual field
    # self.fields['first_name'].widget.attrs.update({'class': 'input input--text', 'id': "formInput#text", 'placeholder': 'Enter your first name...'})
    # self.fields['last_name'].widget.attrs.update({'class': 'input input--text', 'id': "formInput#text", 'placeholder': 'Enter your last name...'})
