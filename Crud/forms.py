from django import forms
from .models import Teams, Users
class TeamForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class UserLoginForm(forms.Form):
    model = Users
    UserName = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)