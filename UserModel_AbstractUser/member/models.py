from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group

from web.models import Customer

class CustomUser(AbstractUser):
    user_name = models.CharField(verbose_name='이름 ', max_length=20)
    user_call = models.CharField(verbose_name='내선 번호 ', max_length=4, blank=True, null=True)
    user_image = models.ImageField(verbose_name='프로필 사진', upload_to='user/', blank=True, null=True)
    team_code = models.ForeignKey(Team, verbose_name='팀 선택 ', on_delete=models.PROTECT, blank=True, null=True)
    rank_code = models.ForeignKey(Rank, verbose_name='직급 선택 ', on_delete=models.PROTECT, blank=True, null=True)
    is_staff = models.BooleanField('관리자 사이트 접속 여부', default=True,)
    create_time = models.DateTimeField('CREATE DATE ', auto_now_add=True)
    update_time = models.DateTimeField('MODIFY DATE ', auto_now=True)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
        db_table = 'x_m_user'
        ordering = ('user_name',)
