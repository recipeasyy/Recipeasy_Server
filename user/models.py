from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from theme.models import Theme


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, realname):
        if not username:
            raise ValueError('must have username')

        if not realname:
            raise ValueError('must have realname')

        user = self.model(
            username=username,
            realname=realname,
        )

        user.save()
        return user

    def create_superuser(self, username, realname, password):
        user = self.create_user(username=username, realname=realname)
        user.set_password(password)
        user.is_staff = True  # 슈퍼유저 권한 부여
        user.is_superuser = True  # 슈퍼유저 권한 부여
        user.save()
        return user


class User(AbstractBaseUser):
    objects = UserManager()

    username = models.CharField(max_length=200, unique=True)
    realname = models.CharField(max_length=20)
    nickname = models.CharField(max_length=50, unique=True, blank=True, null=True) # 추후에 api post 요청으로 닉네임 받아와야함
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    saved_themes = models.ManyToManyField(Theme, related_name='saved_users', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['realname', ]

    class Meta:
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.realname

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
