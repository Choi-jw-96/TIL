from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user',)

    title = forms.CharField(
        label='title',
        widget=forms.TextInput(
          attrs={
            'class' : 'form-control',
            'placeholder' : '글 제목을 입력해주세요',
          }
        )
    )
    content = forms.CharField(
        label='content',
        widget=forms.Textarea(
          attrs={
            'class' : 'form-control',
            'placeholder' : '글 내용을 입력해주세요'
          }
        )
    )
    movie = forms.CharField(
        label='movie',
        widget=forms.TextInput(
          attrs={
            'class' : 'form-control',
            'placeholder' : '영화 제목을 입력해주세요'
          }
        )
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    content = forms.CharField(
        label='content', 
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'style' : 'width : 500px',
            'placeholder' : '댓글을 써주세요'
        }
        )
    )
