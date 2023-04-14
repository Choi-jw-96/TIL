from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget = forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : '제목을 입력해 주세요',
            }
        )
    )


# class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',) 이 필드만 나오게
        # exclude = ('title',) 이 필드는 제외해서