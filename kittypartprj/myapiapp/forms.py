from django import forms

class kunjamu(forms.Form):
    name=forms.CharField(max_length=60,label='name')
    servicetype=forms.ChoiceField(choices=(('nisha','nisha'),('babu','babu')),widget=forms.Select())