from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        fields = ['society', 'member', 'amount', 'date', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Add Transaction'))
