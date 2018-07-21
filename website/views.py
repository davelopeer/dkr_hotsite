from django.shortcuts import render
from website.forms import InscriptionForm, InscriptionFormEn, InscriptionFormEs, HealthForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from website.sendgrid.sg_inscription import sendMail, sendMailHealth
from django.utils import translation

# Create your views here.
def index(request):
    # Discovering the user langugage
    user_language = translation.get_language_from_request(request, check_path=True)

    if request.method == 'POST':
        form = InscriptionForm(request.POST)

        # # SETTING THE REQUIRED PAYMENT ACCORDING TO THE USER LANGUAGE
        # else:
        #     form.fields['payment_international'].required = True
        #
        # # SETTING THE REQUIRED PAYMENT INFO ACCORDING TO SELECTED PAYMENT
        # user_payment = form.fields['payment']
        # if user_payment == 'Cartão de crédito':
        #     form.fields['credit_card_name'].required = True
        #
        # if (form.fields['payment']) == 'Depósito bancário':
        #     form.fields['deposit_day'].required = True
        #     form.fields['deposit_name'].required = True
        #     form.fields['credit_card_name'].required = True

        if form.is_valid():
            name = request.POST.get('name', '')
            birthday = request.POST.get('birthday', '')
            adress = request.POST.get('adress', '')
            adress_num = request.POST.get('adress_num', '')
            adress_comp = request.POST.get('adress_comp', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            gender = request.POST.get('gender', '')
            initiations = request.POST.get('initiations', '')
            initiations_lama = request.POST.get('initiations_lama', '')
            monastic_ordenation = request.POST.get('monastic_ordenation', '')
            observations = request.POST.get('observations', '')
            food_preferency = request.POST.get('food_preferency', '')
            seat = request.POST.get('seat', '')
            payment = request.POST.get('payment', '')
            payment_international = request.POST.get('payment_international', '')
            deposit_day = request.POST.get('deposit_day', '')
            deposit_name = request.POST.get('deposit_name', '')
            deposit_value = request.POST.get('deposit_value', '')
            deposit_agency = request.POST.get('deposit_agency', '')
            deposit_account = request.POST.get('deposit_account', '')
            deposit_envelop = request.POST.get('deposit_envelop', '')
            credit_card_name = request.POST.get('credit_card_name', '')
            paypal_name = request.POST.get('paypal_name', '')
            event_option = request.POST.get('event_option', '')


            #Make the date in the br format dd/mm/yyyy
            def dateBR(date):
                new_date = str(str(date[8:10]) + '/' +  str(date[5:7]) + '/' + str(date[0:4]))
                return new_date

            birthday_br = dateBR(birthday)
            deposit_day_br = dateBR(deposit_day)


            # See if it was paid with credit card or deposit
            if user_language == 'pt-br':
                if payment == 'Cartão de crédito':
                    payment_info = 'Nome do titular do cartão: ' + credit_card_name
                else:
                    payment_info = "Depositado o valor de " + deposit_value + " no dia " + deposit_day_br + " por " + deposit_name + " com os dados: " + "\n" + "\nNúmero do envelope: " + deposit_envelop + "\n    ou" + "\nAgência: " +  deposit_agency + " - Conta: " + deposit_account
            else:
                payment_info = 'Nome do usuário Paypal: ' + paypal_name

            sendMail(
                    name,
                    birthday_br,
                    adress,
                    adress_num,
                    adress_comp,
                    city,
                    state,
                    zip_code,
                    email,
                    phone,
                    gender,
                    initiations,
                    initiations_lama,
                    monastic_ordenation,
                    observations,
                    food_preferency,
                    seat,
                    payment,
                    payment_international,
                    payment_info,
                    event_option,
                    )
            return redirect('pay-success')
    else:
        if user_language == 'pt-br':
            form = InscriptionForm()
        elif user_language == 'es':
            form = InscriptionFormEs()
        else:
            form = InscriptionFormEn()


    return render(request, 'index.html',  {
        'form': form,
        'user_language': user_language
    })

def pay_success(request):
    return render(request, 'pay-success.html')

def cancellation_policy(request):
    return render(request, 'cancellation-policy.html')

def health_form(request):

    user_language = translation.get_language_from_request(request, check_path=True)
    if request.method == 'POST':
        health_form = HealthForm(request.POST)
        if health_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            birthday = request.POST.get('birthday', '')
            medical_agreement = request.POST.get('medical_agreement', '')
            coverage = request.POST.get('coverage', '')
            phone = request.POST.get('phone', '')
            emergency_contact_name = request.POST.get('emergency_contact_name', '')
            emergency_contact_degree = request.POST.get('emergency_contact_degree', '')
            emergency_contact_phone = request.POST.get('emergency_contact_phone', '')
            health_problems = request.POST.get('health_problems', '')
            medicines_alergie = request.POST.get('medicines_alergie', '')
            food_alergie = request.POST.get('food_alergie', '')
            insect_alergie = request.POST.get('insect_alergie', '')
            psychiatric_treatment = request.POST.get('psychiatric_treatment', '')
            medication = request.POST.get('medication', '')
            doctor_name = request.POST.get('doctor_name', '')
            doctor_phone = request.POST.get('doctor_phone', '')
            observations = request.POST.get('observations', '')

            def dateBR(date):
                new_date = str(str(date[8:10]) + '/' +  str(date[5:7]) + '/' + str(date[0:4]))
                return new_date

            birthday_br = dateBR(birthday)

            sendMailHealth(
                    name,
                    email,
                    birthday_br,
                    medical_agreement,
                    coverage,
                    phone,
                    emergency_contact_name,
                    emergency_contact_degree,
                    emergency_contact_phone,
                    health_problems,
                    medicines_alergie,
                    food_alergie,
                    insect_alergie,
                    psychiatric_treatment,
                    medication,
                    doctor_name,
                    doctor_phone,
                    observations,
                    )
            return redirect('index')
    else:
        health_form = HealthForm()

    return render(request, 'health-form.html', {
        'user_language': user_language,
        'health_form': health_form,
    })
