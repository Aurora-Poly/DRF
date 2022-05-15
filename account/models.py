from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, email, name, univ, dept, age, password=None):
    if not email:
      raise ValueError('must have user email')
    if not name:
      raise ValueError('must have user name')
    if not univ:
      raise ValueError('must have user univ')
    if not dept:
      raise ValueError('must have user dept')
    if not age:
      raise ValueError('must have user age')

    user = self.model(
      email = self.normalize_email(email),
      name = name,
      univ = univ,
      dept = dept,
      age = age
    )
    user.set_password(password)
    user.save(using=self.db)
    return user

  def create_superuser(self,email,name, univ, dept, age, password=None ):
    user = self.create_user(
      email,
      password = password,
      name = name,
      univ = univ,
      dept = dept,
      age = age
    )

    user.is_admin = True
    user.is_staff = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):

  def get_full_name(self):
    pass

  def get_short_name(self):
    pass

  @property
  def is_superuser(self):
    return self.is_admin

  @property
  def is_staff(self):
    return self.is_admin

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, app_label):
    return self.is_admin

  id = models.AutoField(primary_key = True)
  email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
  name= models.CharField(default='', max_length=100, null=False, blank=False)
  univ = models.CharField(default='', max_length=100, null=False, blank=False)
  dept = models.CharField(default='', max_length=100, null=False, blank=False)
  age = models.IntegerField(default='', null=False, blank=False)

  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [ 'name', 'univ', 'dept', 'age','password']

  def __str__(self):
    return self.name