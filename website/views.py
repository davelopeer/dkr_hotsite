from django.shortcuts import render
from website.forms import InscriptionForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from website.sendgrid.sg_inscription import sendMail

# Create your views here.
def index(request):
    form_class = InscriptionForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

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
            cancel_terms = request.POST.get('cancel_terms', '')
            deposit_day = request.POST.get('deposit_day', '')
            deposit_name = request.POST.get('deposit_name', '')
            deposit_agency = request.POST.get('deposit_agency', '')
            deposit_envelop = request.POST.get('deposit_envelop', '')
            credit_card_name = request.POST.get('credit_card_name', '')
            # deposit_voucher = request.FILES['deposit_voucher']

            #Make the date in the br format dd/mm/yyyy
            def dateBR(date):
                new_date = str(str(date[8:10]) + '/' +  str(date[5:7]) + '/' + str(date[0:4]))
                return new_date

            birthday_br = dateBR(birthday)
            deposit_day_br = dateBR(deposit_day)

            # birthday_br = str(str(birthday[8:10]) + '/' +  str(birthday[5:7]) + '/' + str(birthday[0:4]))
            # deposit_day_br = str(str(deposit_day[8:10]) + '/' +  str(deposit_day[5:7]) + '/' + str(deposit_day[0:4]))

            # See if it wa paid with credit card or deposit
            if payment == 'Cartão de crédito':
                payment_info = 'Nome do titular do cartão: ' + credit_card_name
            else:
                payment_info = "Depositado no dia " + deposit_day_br + " por " + deposit_name + " com os dados:" + deposit_agency + deposit_envelop



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
                    payment_info,
                    # deposit_voucher,
                    )
            return redirect('index')
        else:
            return redirect('https://docs.djangoproject.com/en/2.0/topics/i18n/translation/ ') #PAGINA QUALQUER DE TESTE

    return render(request, 'base.html', {
        'form': form_class,
    })
