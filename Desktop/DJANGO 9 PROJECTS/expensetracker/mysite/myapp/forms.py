from django import forms 
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["name", "amount", "category"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'}),
            'amount': forms.NumberInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'}),
            'category': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'}),
            'date': forms.DateInput(attrs={'class': 'border border-gray-300 rounded-md py-2 px-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500', 'type': 'date'}),
        }