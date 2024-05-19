from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={"required": "Can't be empty"})
    password = forms.CharField(error_messages={"required": "Can't be empty"})

class SignupForm(forms.Form):
    email = forms.EmailField(error_messages={"required": "Can't be empty"})
    password1 = forms.CharField(error_messages={"required": "Can't be empty"})
    password2 = forms.CharField(error_messages={"required": "Can't be empty"})

    def clean(self):
        cleaned_data = super().clean()
        if self.errors:
            return
            
        if cleaned_data["password1"] != cleaned_data["password2"]:
            self.add_error("password2", "Passwords do not match")
        return cleaned_data
