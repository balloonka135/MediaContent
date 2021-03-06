from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    '''
    Form for User creation.
    '''

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
