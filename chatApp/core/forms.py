from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserCreationForm is an django's form page. 
class SignUpForm(UserCreationForm):
    # The Meta class provide additional information for the Form.
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']