from django.contrib import admin
from .models import Produto, Compra, Retirada
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario

# Register your models here.
@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'setor', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'setor')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('registro', 'nome', 'ca', 'categoria', 'qtd_estoque', 'qtd_estoque_min', 'data_cadastro', 'modificado_em')

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('produto', 'qtd_compra', 'data_compra')

@admin.register(Retirada)
class RetiradaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'qtd_retirada', 'data_retirada')


