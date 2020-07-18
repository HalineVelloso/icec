from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUsuario
from .models import Produto, Compra, Retirada

class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'email', 'setor')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'setor')

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['registro', 'nome', 'ca', 'categoria', 'qtd_estoque', 'qtd_estoque_min']

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ['produto', 'qtd_compra']

class RetiradaForm(forms.ModelForm):

    class Meta:
        model = Retirada
        fields = ['produto', 'qtd_retirada']

