from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib import messages

# Create your models here.

class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    setor = models.CharField('Setor', max_length=30)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'setor']

    def __str__(self):
        return self.email

    objects = UsuarioManager()

class Produto(models.Model):
    registro = models.CharField('ID', max_length=20, help_text='Máximo 20 caracteres', unique=True)
    nome = models.CharField('Nome', max_length=255)
    ca = models.IntegerField('CA')
    categoria = models.CharField('Categoria', max_length=100)
    qtd_estoque = models.IntegerField('Estoque')
    qtd_estoque_min = models.IntegerField('Estoque minimo')
    data_cadastro = models.DateTimeField(default=timezone.now, editable=False)
    modificado_em = models.DateTimeField(default=timezone.now, editable=False)
    
    def save(self, *args, **kwargs):
        self.modificado_em = timezone.now()
        super(Produto, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.registro} - {self.nome}'

class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd_compra = models.IntegerField('Quantidade comprada')
    data_compra = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super(Compra, self).save(*args, **kwargs)
        estoque = Produto.objects.get(id=self.produto.id)
        estoque.qtd_estoque += self.qtd_compra
        estoque.save()

    def __str__(self):
        return f'{self.produto_id} - {self.qtd_compra}'

class Retirada(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd_retirada = models.IntegerField('Quantidade retirada')
    setor_enviado = models.CharField('Setor', max_length=100)
    data_retirada = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        estoque = Produto.objects.get(id=self.produto.id)
        if estoque.qtd_estoque >= self.qtd_retirada:
            super(Retirada, self).save(*args, **kwargs)
            estoque.qtd_estoque -= self.qtd_retirada
            estoque.save()
        else:
            raise Exception('Estoque indisponivel.')

    def __str__(self):
        return f'{self.produto_id} - {self.qtd_retirada}'

