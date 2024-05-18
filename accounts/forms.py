from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

class SignupForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password1"] != cleaned_data["password2"]:
            self.add_error("password2", "Passwords do not match")
        return cleaned_data
