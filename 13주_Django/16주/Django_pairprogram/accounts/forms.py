from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True, 
        label="아이디",
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '영문 소문자 또는 영문 대문자, 숫자 조합 6~12 자리'
        })
    )

    email = forms.EmailField(
        max_length=254, 
        required=True,
        label="이메일",
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '이메일 입력'
        })
    )
        
    first_name = forms.CharField(
        max_length=30,
        required=True, 
        label="이름",
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '이름 입력'
        })
    )

    last_name = forms.CharField(
        max_length=30,
        required=True, 
        label="성",
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '성 입력'
        })
    )

    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '영문, 숫자, 특수문자(~!@#$%^&*) 조합 8~15 자리'
        })
    )

    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '비밀번호 확인'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(
        max_length=254, 
        required=True, 
        label="이메일",
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '이메일 입력'
        })
    )
        
    first_name = forms.CharField(
        max_length=30,
        required=True, 
        label="이름",
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '이름 입력'
        })
    )

    last_name = forms.CharField(
        max_length=30,
        required=True, 
        label="성",
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '성 입력'
        })
    )
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        label="아이디",
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '아이디 입력'
        })
    )

    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '비밀번호 입력'
        })
    )


class CustomUserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="기존 비밀번호",
        widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '기존 비밀번호 입력'
        })
    )

    new_password1 = forms.CharField(
        label="새 비밀번호",
        widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '새 비밀번호 입력'
        })
    )

    new_password2 = forms.CharField(
        label="새 비밀번호 확인",
        widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '새 비밀번호 확인'
        })
    )
