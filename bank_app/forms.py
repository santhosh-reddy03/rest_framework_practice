from django import forms
from django.db.models.base import Model
from .models import Account
class CustomerCreationForm(forms.Form):
    customer_id = forms.IntegerField(label="Customer ID", min_value=100000000, max_value=999999999, required=True)
    customer_ssn_id = forms.IntegerField(label="SSN ID", min_value=100000000, max_value=999999999, required=True)
    age = forms.IntegerField(label="Age", required=True)
    customer_name = forms.CharField(label="Customer Name", max_length=100, required=True)
    address_line1 = forms.CharField(widget=forms.Textarea ,required=True, label="address_lane1")
    address_line2 = forms.CharField(widget=forms.Textarea, label="address_lane2")
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['customer_id', 'account_id', 'account_type', 'amount']

    




