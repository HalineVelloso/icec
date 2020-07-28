import django_filters
from .models import Produto

class ProdutoFilter(django_filters.FilterSet):
    class Meta:
        model = Produto
        fields = ['nome']
    
    def filtro(self, queryset, name, value):
        return queryset.filter(name__contains=value)

"""
class F(django_filters.FilterSet):
    username = CharFilter(method='my_custom_filter')

    class Meta:
        model = User
        fields = ['username']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
"""