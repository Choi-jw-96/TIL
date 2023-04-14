from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# 장고는 직접참조를 권장하지 않음
# from .models import User
# 아래와 같은 간접 참조를 이용한다
# get_user_model 현재 프로젝트에 활성화 되어있는 User객체를 반환해준다
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 우리가 사용하는 User class로 재정의(우리가 accounts를 재정의했기 때문)
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')