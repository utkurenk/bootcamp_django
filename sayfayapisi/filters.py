from .models import *
import django_filters
from django_filters import DateRangeFilter


class TransactionFilter(django_filters.FilterSet):
    Date = DateRangeFilter(label="Tarih")

    def __init__(self, *args, **kwargs):
        super(TransactionFilter, self).__init__(*args, **kwargs)
        self.filters['Category'].label = 'Kategori'
        self.filters['Type'].label = 'Tür'

    class Meta:
        model = Transaction
        fields = "__all__"
        exclude = ["Client", "Date", "Amount"]
