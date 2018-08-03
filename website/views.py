from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import get_template
from django.utils import translation
from django.http import HttpResponseNotFound
from website.forms import InscriptionForm, InscriptionFormEn, InscriptionFormEs, HealthForm, GuestForm, GuestFormEs, GuestFormEn, VolunteerForm, VolunteerFormEn, VolunteerFormEs, SponsorForm, SponsorFormEn, SponsoredForm
from website.sendgrid.sg_inscription import sendMail, sendMailHealth, sendMailVolunteer, sendMailError, sendMailHealthError, sendMailVolunteerError

def index(request):
    user_language = translation.get_language_from_request(request, check_path=True)

    if request.method == 'POST':
        if user_language == 'pt-br':
            form = InscriptionForm(request.POST)
        elif user_language == 'es':
            form = InscriptionFormEs(request.POST)
        else:
            form = InscriptionFormEn(request.POST)

        # if (form.fields['payment']) == 'Depósito bancário':
        #     form.fields['deposit_day'].required = True
        name = request.POST.get('name', '')
        birthday = request.POST.get('birthday', '')
        adress = request.POST.get('adress', '')
        adress_num = request.POST.get('adress_num', '')
        adress_comp = request.POST.get('adress_comp', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
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

        # SET THE PAYMENT_INFO
        if user_language == 'pt-br':
            if payment == 'Cartão de crédito':
                payment_info = 'Nome do titular do cartão: ' + credit_card_name
            else:
                payment_info = "Depositado o valor de " + deposit_value + " no dia " + deposit_day + " por " + deposit_name + " com os dados: <br>" + "Número do envelope: " + deposit_envelop + "<br>ou<br>" + "Agência: " +  deposit_agency + " - Conta: " + deposit_account
        else:
            payment_info = 'Nome do usuário Paypal: ' + paypal_name

        if form.is_valid():
            sendMail(
                    name,
                    birthday,
                    adress,
                    adress_num,
                    adress_comp,
                    city,
                    state,
                    country,
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
            sendMailError(
                    name,
                    birthday,
                    adress,
                    adress_num,
                    adress_comp,
                    city,
                    state,
                    country,
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
            if user_language == 'pt-br':
                return HttpResponseNotFound('<h1>Dados inválidos no formulário. Iremos avaliar os seus dados e entraremos em contato com você. Certifique-se de ter preenchido corretamento o campo e-mail.</h1>')
            elif user_language == 'es':
                return HttpResponseNotFound('<h1>Datos no válidos en el formulario. Nosotros evaluamos sus datos y nos pondremos en contacto con usted. Asegúrese de que ha completado el campo de correo electrónico.</h1>')
            else:
                return HttpResponseNotFound('<h1>Invalid form data. We will evaluate it and will contact you. Make sure your email has been correctly filled.</h1>')

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
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        birthday = request.POST.get('birthday', '')
        medical_agreement = request.POST.get('medical_agreement', '')
        coverage = request.POST.get('coverage', '')
        phone = request.POST.get('phone', '')
        emergency_contact_name = request.POST.get('emergency_contact_name', '')
        emergency_contact_degree = request.POST.get('emergency_contact_degree', '')
        emergency_contact_phone = request.POST.get('emergency_contact_phone', '')
        emergency_contact_email = request.POST.get('emergency_contact_email', '')
        health_problems = request.POST.get('health_problems', '')
        medicines_alergie = request.POST.get('medicines_alergie', '')
        food_alergie = request.POST.get('food_alergie', '')
        insect_alergie = request.POST.get('insect_alergie', '')
        psychiatric_treatment = request.POST.get('psychiatric_treatment', '')
        medication = request.POST.get('medication', '')
        doctor_name = request.POST.get('doctor_name', '')
        doctor_phone = request.POST.get('doctor_phone', '')
        observations = request.POST.get('observations', '')

        if health_form.is_valid():
            sendMailHealth(
                    name,
                    email,
                    birthday,
                    medical_agreement,
                    coverage,
                    phone,
                    emergency_contact_name,
                    emergency_contact_degree,
                    emergency_contact_phone,
                    emergency_contact_email,
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
            sendMailHealthError(
                    name,
                    email,
                    birthday,
                    medical_agreement,
                    coverage,
                    phone,
                    emergency_contact_name,
                    emergency_contact_degree,
                    emergency_contact_phone,
                    emergency_contact_email,
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
            if user_language == 'pt-br':
                return HttpResponseNotFound('<h1>Dados inválidos no formulário. Iremos avaliar os seus dados e entraremos em contato com você. Certifique-se de ter preenchido corretamento o campo e-mail.</h1>')
            elif user_language == 'es':
                return HttpResponseNotFound('<h1>Datos no válidos en el formulario. Nosotros evaluamos sus datos y nos pondremos en contacto con usted. Asegúrese de que ha completado el campo de correo electrónico.</h1>')
            else:
                return HttpResponseNotFound('<h1>Invalid form data. We will evaluate it and will contact you. Make sure your email has been correctly filled.</h1>')
    else:
        health_form = HealthForm()

    return render(request, 'health-form.html', {
        'user_language': user_language,
        'health_form': health_form,
    })


def volunteer_form(request):
    user_language = translation.get_language_from_request(request, check_path=True)
    if request.method == 'POST':
        if user_language == 'pt-br':
            form = VolunteerForm(request.POST)
        elif user_language == 'es':
            form = VolunteerFormEs(request.POST)
        else:
            form = VolunteerFormEn(request.POST)

        name = request.POST.get('name', '')
        birthday = request.POST.get('birthday', '')
        adress = request.POST.get('adress', '')
        adress_num = request.POST.get('adress_num', '')
        adress_comp = request.POST.get('adress_comp', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
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
        physical_problems = request.POST.get('physical_problems', '')
        joint_problems = request.POST.get('joint_problems', '')
        health_problems = request.POST.get('health_problems', '')
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

        if user_language == 'pt-br':
            if payment == 'Cartão de crédito':
                payment_info = 'Nome do titular do cartão: ' + credit_card_name
            else:
                payment_info = "Depositado o valor de " + deposit_value + " no dia " + deposit_day + " por " + deposit_name + " com os dados: <br>" + "Número do envelope: " + deposit_envelop + "<br>ou<br>" + "Agência: " +  deposit_agency + " - Conta: " + deposit_account
        else:
            payment_info = 'Nome do usuário Paypal: ' + paypal_name

        if form.is_valid():
            sendMailVolunteer(
                    name,
                    birthday,
                    adress,
                    adress_num,
                    adress_comp,
                    city,
                    state,
                    country,
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
                    physical_problems,
                    joint_problems,
                    health_problems,
                    payment,
                    payment_international,
                    payment_info,
                    event_option,
                    )
            return redirect('pay-success')

        else:
            sendMailVolunteerError(
                    name,
                    birthday,
                    adress,
                    adress_num,
                    adress_comp,
                    city,
                    state,
                    country,
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
                    physical_problems,
                    joint_problems,
                    health_problems,
                    payment,
                    payment_international,
                    payment_info,
                    event_option,
                    )
            if user_language == 'pt-br':
                return HttpResponseNotFound('<h1>Dados inválidos no formulário. Iremos avaliar os seus dados e entraremos em contato com você. Certifique-se de ter preenchido corretamento o campo e-mail.</h1>')
            elif user_language == 'es':
                return HttpResponseNotFound('<h1>Datos no válidos en el formulario. Nosotros evaluamos sus datos y nos pondremos en contacto con usted. Asegúrese de que ha completado el campo de correo electrónico.</h1>')
            else:
                return HttpResponseNotFound('<h1>Invalid form data. We will evaluate it and will contact you. Make sure your email has been correctly filled.</h1>')

    else:
        if user_language == 'pt-br':
            form = VolunteerForm()
        elif user_language == 'es':
            form = VolunteerFormEs()
        else:
            form = VolunteerFormEn()

    return render(request, 'volunteer-form.html', {
        'form': form,
        'user_language': user_language,
    })

def guest_form(request):
    user_language = translation.get_language_from_request(request, check_path=True)

    if request.method == 'POST':
        if user_language == 'pt-br':
            form = GuestForm(request.POST)
        elif user_language == 'es':
            form = GuestFormEs(request.POST)
        else:
            form = GuestFormEn(request.POST)

        # if (form.fields['payment']) == 'Depósito bancário':
        #     form.fields['deposit_day'].required = True
        name = request.POST.get('name', '')
        birthday = request.POST.get('birthday', '')
        adress = request.POST.get('adress', '')
        adress_num = request.POST.get('adress_num', '')
        adress_comp = request.POST.get('adress_comp', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
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

        # SET THE PAYMENT_INFO
        if user_language == 'pt-br':
            if payment == 'Cartão de crédito':
                payment_info = 'Nome do titular do cartão: ' + credit_card_name
            else:
                payment_info = "Depositado o valor de " + deposit_value + " no dia " + deposit_day + " por " + deposit_name + " com os dados: <br>" + "Número do envelope: " + deposit_envelop + "<br>ou<br>" + "Agência: " +  deposit_agency + " - Conta: " + deposit_account
        else:
            payment_info = 'Nome do usuário Paypal: ' + paypal_name

        if form.is_valid():
            sendMail(
                    name,
                    birthday,
                    adress,
                    adress_num,
                    adress_comp,
                    city,
                    state,
                    country,
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
            sendMailError(
                    name,
                    birthday,
                    adress,
                    adress_num,
                    adress_comp,
                    city,
                    state,
                    country,
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
            if user_language == 'pt-br':
                return HttpResponseNotFound('<h1>Dados inválidos no formulário. Iremos avaliar os seus dados e entraremos em contato com você. Certifique-se de ter preenchido corretamento o campo e-mail.</h1>')
            elif user_language == 'es':
                return HttpResponseNotFound('<h1>Datos no válidos en el formulario. Nosotros evaluamos sus datos y nos pondremos en contacto con usted. Asegúrese de que ha completado el campo de correo electrónico.</h1>')
            else:
                return HttpResponseNotFound('<h1>Invalid form data. We will evaluate it and will contact you. Make sure your email has been correctly filled.</h1>')

    else:
        if user_language == 'pt-br':
            form = GuestForm()
        elif user_language == 'es':
            form = GuestFormEs()
        else:
            form = GuestFormEn()


    return render(request, 'guest-form.html',  {
        'form': form,
        'user_language': user_language
    })


def sponsor(request):
    user_language = translation.get_language_from_request(request, check_path=True)

    if request.method == 'POST':

        sponsored_form = Sponsored(request.POST)
        if user_language == 'pt-br':
            sponsor_form = Sponsor(request.POST)
        else:
            sponsor_form = SponsorEn(request.POST)

        # if (form.fields['payment']) == 'Depósito bancário':
        #     form.fields['deposit_day'].required = True

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
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
        sangha = request.POST.get('sangha', '')

        # SET THE PAYMENT_INFO
        if user_language == 'pt-br':
            if payment == 'Cartão de crédito':
                payment_info = 'Nome do titular do cartão: ' + credit_card_name
            else:
                payment_info = "Depositado o valor de " + deposit_value + " no dia " + deposit_day + " por " + deposit_name + " com os dados: <br>" + "Número do envelope: " + deposit_envelop + "<br>ou<br>" + "Agência: " +  deposit_agency + " - Conta: " + deposit_account
        else:
            payment_info = 'Nome do usuário Paypal: ' + paypal_name

        if form.is_valid():
            sendMailSponsor(
                    name,
                    email,
                    phone,
                    payment,
                    payment_international,
                    payment_info,
                    )
            return redirect('pay-success')

        else:
            sendMailError(
                    name,
                    email,
                    phone,
                    payment,
                    payment_international,
                    payment_info,
                    )
            if user_language == 'pt-br':
                return HttpResponseNotFound('<h1>Dados inválidos no formulário. Iremos avaliar os seus dados e entraremos em contato com você. Certifique-se de ter preenchido corretamento o campo e-mail.</h1>')
            elif user_language == 'es':
                return HttpResponseNotFound('<h1>Datos no válidos en el formulario. Nosotros evaluamos sus datos y nos pondremos en contacto con usted. Asegúrese de que ha completado el campo de correo electrónico.</h1>')
            else:
                return HttpResponseNotFound('<h1>Invalid form data. We will evaluate it and will contact you. Make sure your email has been correctly filled.</h1>')

    else:
        sponsored_form = Sponsored()
        if user_language == 'pt-br':
            sponsor_form = Sponsor()
        else:
            sponsor_form = SponsorEn()


    return render(request, 'sponsor-form.html',  {
        'sponsored_form': sponsored_form,
        'sponsor_form': sponsor_form,
        'user_language': user_language
    })
