from django import forms
from django.utils.translation import ugettext_lazy as _


# FORMULÁRIO BASE

class GeneralForm(forms.Form):
    name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.CharField(required=True,max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    adress = forms.CharField(required=True, max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    adress_num = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    adress_comp = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(required=True, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100, widget=forms.EmailInput(attrs={'type':'email', 'class':'form-control'}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'type':'number','class': 'form-control'}))
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check'}), choices=(
        ('Masculino',_('Male')),
        ('Feminino',_('Female')),
        ('Outro',_('Other')),
    ))
    initiations = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area'}))
    initiations_lama = forms.CharField(required=True,max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area'}))
    monastic_ordenation = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'value':'1','type':'radio', 'class':'form-check inline'}), choices=(
        ('Sim',_('Yes')),
        ('Não',_('No')),
    ))
    food_preferency = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline food-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Não-vegetariana',_('Non vegetarian')),
        ('Vegetariana',_('Vegetarian')),
    ))
    seat = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check seat-preferency', 'data-toggle':'modal', 'data-target':'#exampleModal'}), choices=(
        ('Sim',_('Yes')),
        ('Não',_('No')),
    ))

    observations = forms.CharField(required=False,max_length=4000, widget=forms.Textarea(attrs={'name':'observations','class': 'form-control form_text_area'}))
    # BR PAYMENT
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
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
        ))
    # OTHER PAYMENTS
    payment_international = forms.ChoiceField(required=False, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline'}), choices=(
        ('PayPal',''),
    ))
    paypal_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',  }))
    cancel_terms = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'checkbox', 'class':'form-check'}), choices=(
        ('Aceito',''),
    ))

# MAIN INSCRIPTION FORM

class InscriptionForm(GeneralForm, forms.Form):
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Adulto',_('Adult full event with three meals and no lodging: US$ 809.05')),
        ('Criança 4-12 anos',_('Children from 4 to 12 years old with three meals and no lodging: US$ 258.52')),
        ('Criança 0-3 anos',_('Children from 0 to 3 years old with three meals and no lodging: Free')),
    ))

# HEALTH FORM

class HealthForm(GeneralForm,forms.Form):
    medical_agreement = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    coverage = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
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

# FORM TO GUESTS THAT WILL STAY IN IN KHADRO LING

class GuestForm(GeneralForm, forms.Form):
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Adulto',_('Adult full event with three meals and lodging at Khadro Ling: US$ 996.00')),
        ('Criança 4-12 anos',_('Children from 4 to 12 years old with three meals and lodging at Khadro Ling: US$ 446.00')),
        ('Criança 0-3 anos',_('Children from 0 to 3 years old with three meals and no lodging: Free')),
    ))

# FORMULÁRIO DE VOLUNTÁRIOS

class VolunteerForm(GeneralForm, forms.Form):
    physical_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    joint_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    health_problems = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control form_text_area',}))
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Voluntário',_('Alimentación durante el drubchen con alojamiento en la Casa de Retiro: US$ 146.50')),
    ))
    #('Voluntário','Alimentação durante o drubchen com hospedagem na Casa de Retiro: R$ 550,00'),

# FORMULÁRIO PARA PATROCINADORES

class SponsorForm(GeneralForm, forms.Form):
    pass

class SponsoredForm(GeneralForm, forms.Form):
    sangha = forms.CharField(required=True,max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control form_text_area'}))

# FORMULÁRIO PARA INSCRIÇÃO DE PATROCINADOS

class InscriptionSponsoredForm(GeneralForm, forms.Form):
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('Patrocínio',_('Sponsorship')),
    ))
#('Patrocínio','Patrocínio'),
#('Patrocínio','Patrocinio')


# FORMULÁRIO INSCRIÇÃO PARA CONVIDADOS SEM PAGAR O EVENTO

class SpecialGuestForm(GeneralForm, forms.Form):
    event_option = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'type':'radio', 'class':'form-check inline checkbox-option'}), choices=(
        ('',_('')),
    ))
