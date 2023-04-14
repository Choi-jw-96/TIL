from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category',)
        
    title = forms.CharField(
        label='title',
        widget= forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : '글 제목을 입력해주세요.',
        }
        )
    )
    
    content = forms.CharField(
        label='content',
        widget= forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : '내용 제목을 입력해주세요.',
        }
        )
    )
    
    category_choices = [
        ('개발', '개발'),
        ('CS', 'CS'),
        ('신기술', '신기술')
    ]
    category = forms.ChoiceField(
        choices = category_choices,
        label='category',
        widget= forms.Select(
        attrs={
            'class' : 'form-control',
        }
        )
    )