from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client


class ClientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=17, required=True)
    address = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(ClientRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        # Создание профиля клиента
        client = Client.objects.create(user=user,
                                       phone_number=self.cleaned_data['phone_number'],
                                       email=self.cleaned_data['email'],
                                       address=self.cleaned_data.get('address', ''))
        return user