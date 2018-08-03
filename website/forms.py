from django import forms


# FORMULÁTIO DE INSCRIÇÃO


class InscriptionForm(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/01/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Endereço', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Número', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'casa 1', 'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Cidade', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Estado', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, max_length=15, widget=forms.TextInput(attrs={'placeholder': 'CEP', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Somente números', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
        ('Outro','Outro'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
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
        ('Criança 4-12 anos','Participação infantil (de 4 a 12 anos) com as três refeições incluídas e sem hospedagem: R$ 972,00'),
        ('Criança 0-3 anos','Crianças (de 0 a 3 anos) com as três refeições incluídas e sem hospedagem: Isentas'),
    ))
    payment = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Cartão de crédito','Cartão de crédito'),
        ('Depósito bancário','Depósito bancário'),
    ))
    credit_card_name = forms.CharField(required=False,max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', }))
    deposit_day = forms.CharField(required=False, max_length=40, widget=forms.TextInput(attrs={'placeholder':'20/09/2018','class': 'form-control',  }))
    deposit_name = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit_value = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control' }))
    deposit_agency = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    deposit_account = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit_envelop = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))

class InscriptionFormEs(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nombre completo', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/01/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Dirección', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Número', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'casa 1', 'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Departamento/ Región', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Código Postal', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Sólo números', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Masculino'),
        ('Feminino','Femenino'),
        ('Outro','Otro'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Si'),
        ('Não','No'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','No vegetariana'),
        ('Vegetariana','Vegetariana'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Si'),
        ('Não','No'),
    ))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Adulto','Evento completo, incluye tres comidas al día, sin hospedaje: US$ 809.05'),
        ('Criança 4-12 anos','Participación infantil (4 a 12 años) incluye tres comidas al día, sin hospedaje: US$ 258.52'),
        ('Criança 0-3 anos','Participación infantil (de 0 a 3 ãnos) incluye tres comidas al día, sin hospedaje: Isentas'),
    ))
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    paypal_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))

class InscriptionFormEn(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/25/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Adress', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Number', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Zip-code', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'example@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Numbers only', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Male'),
        ('Feminino','Female'),
        ('Outro','Other'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Yes'),
        ('Não','No'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','Non vegetarian'),
        ('Vegetariana','Vegetarian'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Yes'),
        ('Não','No'),
    ))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Adulto','Adult full event with three meals and no lodging: US$ 809.05'),
        ('Criança 4-12 anos','Children from 4 to 12 years old with three meals and no lodging: US$ 258.52'),
        ('Criança 0-3 anos','Children from 0 to 3 years old with three meals and no lodging: Free'),
    ))
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    paypal_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))

# FORMULÁRIO DE SAÚDE

class HealthForm(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'type':'email', 'class':'form-control'}))
    birthday = forms.CharField(required=True, widget=forms.TextInput(attrs={'max':'2999-12-31', 'class': 'form-control'}))
    medical_agreement = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    coverage = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone =  forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'type':'number','class': 'form-control'}))
    emergency_contact_name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_contact_degree = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_contact_phone =  forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number', 'class': 'form-control'}))
    emergency_contact_email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'type':'email', 'class':'form-control'}))
    health_problems = forms.CharField(required=True,max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control form_text_area' }))
    medicines_alergie = forms.CharField(required=True, max_length=400, widget=forms.TextInput(attrs={'class': 'form-control'}))
    food_alergie = forms.CharField(required=True, max_length=400, widget=forms.TextInput(attrs={'class': 'form-control'}))
    insect_alergie = forms.CharField(required=True, max_length=400, widget=forms.TextInput(attrs={'class': 'form-control'}))
    psychiatric_treatment = forms.CharField(required=True, max_length=400, widget=forms.TextInput(attrs={'class': 'form-control'}))
    medication = forms.CharField(required=True, max_length=400, widget=forms.TextInput(attrs={'class': 'form-control'}))
    doctor_name = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    doctor_phone =  forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'type':'number', 'class': 'form-control'}))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area'}))


# FORMULÁRIO DE CONVIDADOS


class GuestForm(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/01/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Endereço', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Número', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'casa 1', 'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Cidade', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Estado', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, max_length=15, widget=forms.TextInput(attrs={'placeholder': 'CEP', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Somente números', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
        ('Outro','Outro'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','Não-vegetariana'),
        ('Vegetariana','Vegetariana'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Adulto','Evento completo com as três refeições incluídas e hospedagem no Khadro Ling: R$ 3.744,00'),
        ('Criança 4-12 anos','Participação infantil (de 4 a 12 anos) com as três refeições incluídas e hospedagem no Khadro Ling: R$ 1.674,00'),
        ('Criança 0-3 anos','Crianças (de 0 a 3 anos) com as três refeições incluídas e sem hospedagem: Isentas'),
    ))
    payment = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Cartão de crédito','Cartão de crédito'),
        ('Depósito bancário','Depósito bancário'),
    ))
    credit_card_name = forms.CharField(required=False,max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', }))
    deposit_day = forms.CharField(required=False, max_length=40, widget=forms.TextInput(attrs={'placeholder':'20/09/2018','class': 'form-control',  }))
    deposit_name = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit_value = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control' }))
    deposit_agency = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    deposit_account = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit_envelop = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))

class GuestFormEs(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nombre completo', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/01/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Dirección', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Número', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'casa 1', 'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Departamento/ Región', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Código Postal', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Sólo números', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Masculino'),
        ('Feminino','Femenino'),
        ('Outro','Otro'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Si'),
        ('Não','No'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','No vegetariana'),
        ('Vegetariana','Vegetariana'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Si'),
        ('Não','No'),
    ))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Adulto','Evento completo, incluye tres comidas al día y hospedaje en Khadro Ling: US$ 996.00'),
        ('Criança 4-12 anos','Participación infantil (4 a 12 años) incluye tres comidas al día y hospedaje en Khadro Ling: US$ 446.00'),
        ('Criança 0-3 anos','Participación infantil (de 0 a 3 ãnos) incluye tres comidas al día y hospedaje en Khadro Ling: Isentas'),
    ))
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    paypal_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))

class GuestFormEn(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/25/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Adress', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Number', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Zip-code', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'example@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Numbers only', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Male'),
        ('Feminino','Female'),
        ('Outro','Other'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Yes'),
        ('Não','No'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','Non vegetarian'),
        ('Vegetariana','Vegetarian'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Yes'),
        ('Não','No'),
    ))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Adulto','Adult full event with three meals and lodging at Khadro Ling: US$ 996.00'),
        ('Criança 4-12 anos','Children from 4 to 12 years old with three meals and lodging at Khadro Ling: US$ 446.00'),
        ('Criança 0-3 anos','Children from 0 to 3 years old with three meals and no lodging: Free'),
    ))
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    paypal_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))


# FORMULÁRIO DE VOLUNTÁRIOS


class VolunteerForm(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/01/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Endereço', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Número', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'casa 1', 'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Cidade', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Estado', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, max_length=15, widget=forms.TextInput(attrs={'placeholder': 'CEP', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Somente números', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
        ('Outro','Outro'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','Não-vegetariana'),
        ('Vegetariana','Vegetariana'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Sim'),
        ('Não','Não'),
    ))
    physical_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    joint_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    health_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Voluntário','Alimentação durante o drubchen com hospedagem na Casa de Retiro: R$ 550,00'),
    ))
    payment = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Cartão de crédito','Cartão de crédito'),
        ('Depósito bancário','Depósito bancário'),
    ))
    credit_card_name = forms.CharField(required=False,max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', }))
    deposit_day = forms.CharField(required=False, max_length=40, widget=forms.TextInput(attrs={'placeholder':'20/09/2018','class': 'form-control',  }))
    deposit_name = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit_value = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control' }))
    deposit_agency = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    deposit_account = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit_envelop = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))

class VolunteerFormEs(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nombre completo', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/01/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Dirección', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Número', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'casa 1', 'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Departamento/ Región', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'País', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Código Postal', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'exemplo@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Sólo números', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Masculino'),
        ('Feminino','Femenino'),
        ('Outro','Otro'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Si'),
        ('Não','No'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','No vegetariana'),
        ('Vegetariana','Vegetariana'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Si'),
        ('Não','No'),
    ))
    physical_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    joint_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    health_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Voluntário','Alimentación durante el drubchen con alojamiento en la Casa de Retiro: US$ 146.50'),
    ))
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    paypal_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))

class VolunteerFormEn(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'form-control',  }))
    birthday = forms.CharField(required=True,max_length=40, widget=forms.TextInput(attrs={'placeholder': '11/25/1980', 'class': 'form-control',  }))
    adress = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Adress', 'class': 'form-control',  }))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':'Number', 'class': 'form-control',  }))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control',  }))
    state = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control',  }))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control'}))
    zip_code = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Zip-code', 'class': 'form-control',  }))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'example@email.com', 'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','placeholder': 'Numbers only', 'class': 'form-control',  }))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino','Male'),
        ('Feminino','Female'),
        ('Outro','Other'),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',  }))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim','Yes'),
        ('Não','No'),
    ))
    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area',  }))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana','Non vegetarian'),
        ('Vegetariana','Vegetarian'),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim','Yes'),
        ('Não','No'),
    ))
    physical_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    joint_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    health_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Voluntário','Alimentación durante el drubchen con alojamiento en la Casa de Retiro: US$ 146.50'),
    ))
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    paypal_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))


class Sponsor(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number', 'class': 'form-control'}))
    payment = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Cartão de crédito','Cartão de crédito'),
        ('Depósito bancário','Depósito bancário'),
    ))
    credit_card_name = forms.CharField(required=False,max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', }))
    deposit_day = forms.CharField(required=False, max_length=40, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    deposit_name = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit_value = forms.CharField(required=False, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control' }))
    deposit_agency = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    deposit_account = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deposit_envelop = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class SponsorEn(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number', 'class': 'form-control'}))
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    paypal_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',  }))

class Sponsored(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'type':'email', 'class':'form-control', 'id':'formGroupExampleInput'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number', 'class': 'form-control'}))
    sangha = forms.CharField(required=True,max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area'}))
