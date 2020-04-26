from django.forms import ModelForm
from django import forms
from django.forms import DateInput

from account.models import User

'''
forms-widgets - assign calendar widget to "date of birth" field.

forms-model-extra - (edit profile form has been done with forms.ModelForm
'''


class SignUpForm(ModelForm):
    date_of_birth = forms.DateField(widget=DateInput(attrs={'type': 'date', 'class': 'datepicker'}))
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'phone','date_of_birth','password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['confirm_password']:
                raise forms.ValidationError('Passwords do not match!')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.save()
        return user


class CustomUserEditForm(ModelForm):
    date_of_birth = forms.DateField(widget=DateInput(attrs={'type': 'date', 'class': 'datepicker'}))

    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name', 'last_name', 'date_of_birth', 'bio')
