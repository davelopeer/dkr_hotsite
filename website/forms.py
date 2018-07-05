from django import forms

class InscriptionForm(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Pema João da Silva ', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    birthday = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder':'01/01/1980','type':'date', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Estr. Linha Águas Brancas', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'1211', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'casa 1', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Três Coroas', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    state = forms.CharField(required=True, max_length=2, widget=forms.TextInput(attrs={'placeholder': 'RS', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    zip_code = forms.CharField(required=True, min_length=9, max_length=9, widget=forms.TextInput(attrs={'placeholder': '95660-000', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': '51 998765432', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
        ('Outro','Outro'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Iniciação de Tara Vermelha, Guru Rinpoche...', 'class': 'form-control form_text_area', 'id': 'formGroupExampleInput'}))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'S. E. Chagdud Tulku Rinpoche, S. E. Dzongsar Khyentse Rinpoche...', 'class': 'form-control form_text_area', 'id': 'formGroupExampleInput'}))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area', 'id': 'formGroupExampleInput'}))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Não-vegetariana','Não-vegetariana'),
        ('Vegetariana','Vegetariana'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    payment = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Cartão de crédito','Cartão de crédito'),
        ('Depósito bancário','Depósito bancário'),
    ))
    credit_card_name = forms.CharField(required=False,max_length=200, widget=forms.TextInput(attrs={'placeholder': 'JOSÉ M R SILVA', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    deposit_day = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder':'20/09/2018','type':'date', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    deposit_name = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'placeholder': 'José M R Silva', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    deposit_agency = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'ag 2856 c/c 008710', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    deposit_envelop = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'1.292.510.482', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))
