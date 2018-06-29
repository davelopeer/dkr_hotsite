import sendgrid
import os
from sendgrid.helpers.mail import *


def sendMail(name,birthday_br,adress,adress_num,adress_comp,city,state,zip_code,email,phone,gender,initiations,initiations_lama,monastic_ordenation,observations,food_preferency,seat,payment,payment_info):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(email)
        to_email = Email("davidbarenco@gmail.com")
        subject = "Formulário de inscrição - Khadro Sangdu"
        sendgrid_content = Content("text", 'DADOS PESSOAIS' + '\n' + '\n' +
                                    'Nome: ' + name + '\n' + '\n'
                                    'Data de nascimento: ' + birthday_br + '\n' + '\n' +
                                    'Endereço: ' + adress + '\n' + '\n' +
                                    'Número: ' + adress_num + '\n' + '\n' +
                                    'Complemento: ' + adress_comp + '\n' + '\n' +
                                    'Cidade: ' + city + '\n' + '\n' +
                                    'Estado: ' + state + '\n' + '\n' +
                                    'CEP: ' + zip_code + '\n' + '\n' +
                                    'E-mail: ' + email + '\n' + '\n' +
                                    'Telefone/celular: ' + phone + '\n' + '\n' +
                                    'Gênero: ' + gender + '\n' + '\n' + '\n' + '\n' +
                                    'Iniciações: ' + '\n' + '\n' + initiations + '\n' + '\n' + '\n' +
                                    'Professores que concederam as iniciações: ' + '\n' + '\n' + initiations_lama + '\n' + '\n' + '\n' +
                                    'Ordenação monástica: ' + monastic_ordenation + '\n' + '\n' +
                                    'Observações gerais: ' + '\n' + '\n' + observations + '\n' + '\n' + '\n' + '\n' +
                                    'Preferência alimentar: ' + food_preferency + '\n' + '\n' +
                                    'Necessidade de cadeira: ' + seat + '\n' + '\n' +
                                    'Forma de pagamento: ' + payment + '\n' + '\n'
                                    'Dados do pagamento: ' + payment_info + '\n' + '\n'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)
        # mail.add_attachment(deposit_voucher)

        response = sg.client.mail.send.post(request_body=mail.get())
        print("success")
        print(response.status_code)
        print(response.body)
        print(response.headers)
