from .models import Articles
from django.forms import ModelForm, TextInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'int_rate', 'max_loan', 'min_dep', 'loan_term']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bank name'
            }),
            'int_rate': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Interest Rate'
            }),
            'max_loan': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Maximum Loan'
            }),
            'min_dep': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minimum Deposit'
            }),
            'loan_term': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Loan Term'
            })

        }
