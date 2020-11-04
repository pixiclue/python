from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from member.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',  'email',)
        labels = {
            'username': '사용자 ID',
            'password2': '비밀번호 확인'
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
        labels = {
            'username': '사용자 ID',
            'password2': '비밀번호 확인'
        }
