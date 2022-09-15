from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError("メールアドレスを入力してください")

        if not name:
            raise ValueError("ユーザー名を入力してください")

        user = self.model(email=self.normalize_email(email), name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):

        user = self.create_user(
            email=email,
            name=name,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="メールアドレス", max_length=256, unique=True)
    name = models.CharField(verbose_name="ユーザー名", max_length=16, unique=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="ユーザー", default=True)
    is_staff = models.BooleanField(verbose_name="スタッフ", default=False)
    is_admin = models.BooleanField(verbose_name="管理者", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
