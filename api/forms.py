from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import CustomUser


class CustomUserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    argentum_id = forms.IntegerField(label='ASDASDASD')
    class Meta:
        model = CustomUser
        fields = ('argentum_id',)

    def clean_argentum_id(self):
        argentum_id = self.cleaned_data.get('argentum_id')
        if argentum_id <= 0:
            raise forms.ValidationError('Argentum id must be greater than zero')
        qs = CustomUser.objects.filter(argentum_id=argentum_id)
        if qs.exists():
            raise forms.ValidationError('Another employee has the same argentum id')
        return argentum_id
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

class CustomUserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    argentum_id = forms.IntegerField(label='Argentum Id')

    class Meta:
        model = CustomUser
        fields = ('argentum_id',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CustomUserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()
    argentum_id = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('password', 'argentum_id')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
    
    def clean_argentum_id(self):
        return self.initial['argentum_id']
# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ('argentum_id',)


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields