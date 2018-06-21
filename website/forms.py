from django import forms

class InscriptionForm(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Pema João da Silva ', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':"email", 'class':'form-control', 'id':'formGroupExampleInput'}))
    # phone = forms.CharField(min_length=11, max_length=15,widget=forms.TextInput(attrs={'class':'form-control', 'id':'formGroupExampleInput', 'placeholder':"Ex:(051)998695682"}))
    phone = forms.IntegerField()
