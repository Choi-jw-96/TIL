from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms



class CustomUserCreationForm(UserCreationForm):        
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2' )

    username = forms.CharField(
        label='username',
        widget= forms.TextInput(
          attrs={
            'class' : 'form-control w-50',
            'placeholder' : '닉네임을 입력해주세요',
          }
        )
    )

    email = forms.EmailField(
        label='email',
        widget= forms.EmailInput(
          attrs={
            'class' : 'form-control w-50',
            'placeholder' : '이메일을 입력해주세요',
          }
        )
    )

    first_name = forms.CharField(
        label="first name",
        widget=forms.TextInput(
          attrs={
            'class' : 'form-control w-50',
            'placeholder' : '성을 입력해주세요',
          }
        )
    )

    last_name = forms.CharField(
        label="last name",
        widget=forms.TextInput(
          attrs={
            'class' : 'form-control w-50',
            'placeholder' : '이름을 입력해주세요',
          }
        )
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput({
          'class' : 'form-control w-50',
          'placeholder' : '비밀번호를 입력해주세요.'
          }
        )
    )

    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput({
          'class' : 'form-control w-50',
          'placeholder' : '비밀번호를 다시 입력해주세요.'
          }
        )
    )



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')

        field_classes = {'email' : EmailField}

    
    email = forms.EmailField(
        label='email',
        widget= forms.EmailInput(
          attrs={
            'class' : 'form-control w-50',
            'placeholder' : '이메일을 입력해주세요',
          }
        )
    )

    first_name = forms.CharField(
        label="first name",
        widget=forms.TextInput(
          attrs={
            'class' : 'form-control w-50',
            'placeholder' : '성을 입력해주세요',
          }
        )
    )

    last_name = forms.CharField(
        label="last name",
        widget=forms.TextInput(
          attrs={
            'class' : 'form-control w-50',
            'placeholder' : '이름을 입력해주세요',
          }
        )
    )
