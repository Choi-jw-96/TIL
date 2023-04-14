from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # user_id 출력을 지워줌
        fields = ('title', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

