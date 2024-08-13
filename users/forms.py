from django import forms

from users.exceptions import RegistrationException
from users.models import User


class PhoneLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=12, label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        # Validate the phone number here (e.g., check if it's in a valid format)
        return phone_number


class UserRegistrationForm(forms.Form):
    phone_number = forms.CharField(max_length=12, required=True, label="Phone Number")
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(widget=forms.TextInput())
    invite_code = forms.CharField(widget=forms.TextInput())

    error_messages = {
        "invalid_login": (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": "This account is inactive.",
    }

    class Meta:
        model = User
        fields = [
            "username",
            "phone_number",
            "password1",
            "password2",
            "invite_code",
            "accept_terms",
        ]

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise RegistrationException("Password cần tối thiểu 8 kí tự!")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise RegistrationException(
                "Xác nhận mật khẩu không trùng nhau!"
            )
        return password2

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if User.objects.filter(phone_number=phone_number).exists():
            raise RegistrationException("Số điện thoại đã được sử dụng.")
        return phone_number

    def save(self, *args, **kwargs):
        phone_number = self.cleaned_data.get("phone_number")
        username = self.cleaned_data.get("username")
        password1 = self.cleaned_data.get("password1")

        user = User.objects._create_user(
            username=username,
            phone_number=phone_number,
            password=password1,
            credit_score=100,
        )
        return user
