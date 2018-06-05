from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from .models import stores
user = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("This user does not exit")              
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.validationError("This user is not longer active")
        return super(UserLoginForm,self).clean(*args,**kwargs)



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = stores
        fields = [
                'firstname',
                'lastname',
                'emailadd'
            ]
        def clean_email(self):
            email = self.cleaned_data.get('emailadd')
            email_qs = stores.objects.filter(email = email)
            if email_qs.exits():
                raise forms.validationError("this email has already been registered")
            return email

