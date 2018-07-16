from django import forms

class InscriptionForm(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    birthday = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder':'01/01/1980','type':'date', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Endereço', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Número', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'casa 1', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Cidade', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    state = forms.CharField(required=True, max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Estado', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    zip_code = forms.CharField(required=True, min_length=9, max_length=9, widget=forms.TextInput(attrs={'placeholder': 'CEP', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Somente números', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
        ('Outro','Outro'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Ex: Iniciação de Guru Rinpoche...', 'class': 'form-control form_text_area', 'id': 'formGroupExampleInput'}))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Ex: S. E. Dzongsar Khyentse Rinpoche...', 'class': 'form-control form_text_area', 'id': 'formGroupExampleInput'}))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area', 'id': 'formGroupExampleInput'}))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','Não-vegetariana'),
        ('Vegetariana','Vegetariana'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Adulto','Evento completo com as três refeições incluídas e sem hospedagem: R$ 3.042,00'),
        ('Criança 4-13 anos','Participação infantil (de 4 a 12 anos) com as três refeições incluídas e sem hospedagem: R$ 972,00'),
        ('Criança 0-3 anos','Crianças (de 0 a 3 anos) com as três refeições incluídas e sem hospedagem: Isentas'),
    ))
    payment = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Cartão de crédito','Cartão de crédito'),
        ('Depósito bancário','Depósito bancário'),
    ))
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    credit_card_name = forms.CharField(required=False,max_length=200, widget=forms.TextInput(attrs={'placeholder': 'JOSÉ M R SILVA', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    deposit_day = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder':'20/09/2018','type':'date', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    deposit_name = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'placeholder': 'José M R Silva', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    deposit_agency = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'ag 2856 c/c 008710', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    deposit_envelop = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'1.292.510.482', 'class': 'form-control', 'id': 'formGroupExampleInput'}))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))
