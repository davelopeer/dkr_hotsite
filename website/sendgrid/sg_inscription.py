import sendgrid
import os
from sendgrid.helpers.mail import *
# import pdb; pdb.set_trace()



def sendMail(name,birthday_br,adress,adress_num,adress_comp,city,state,zip_code,email,phone,gender,initiations,initiations_lama,monastic_ordenation,observations,food_preferency,seat,payment, payment_international,payment_info,event_option):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(email)
        to_email = Email(os.environ.get('DEFAULT_TO_EMAIL'), 'david.barenco@hotmail.com')
        subject = "Formulário de inscrição - Drubchen de Khadro Sangdu"
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
                                    'Gênero: ' + gender + '\n' + '\n' +
                                    'Iniciações: ' + '\n' + '\n' + initiations + '\n' + '\n' + '\n' +
                                    'Professores que concederam as iniciações: ' + '\n' + '\n' + initiations_lama + '\n' + '\n' + '\n' +
                                    'Ordenação monástica: ' + monastic_ordenation + '\n' + '\n' +
                                    'Observações gerais: ' + '\n' + '\n' + observations + '\n' + '\n' +
                                    'Preferência alimentar: ' + food_preferency + '\n' + '\n' +
                                    'Necessidade de cadeira: ' + seat + '\n' + '\n' +
                                    'Opção de evento: ' + event_option + '\n' + '\n' +
                                    'Forma de pagamento: ' + payment + payment_international + '\n' + '\n' +
                                    'Dados do pagamento: ' + payment_info + '\n' + '\n'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)

        u_mail = mail.encode('utf-8')

        response = sg.client.mail.send.post(request_body=u_mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)


def sendMailHealth(name,email,birthday_br,medical_agreement,coverage,phone,emergency_contact_name,emergency_contact_degree,emergency_contact_phone, emergency_contact_email,health_problems,medicines_alergie,food_alergie,insect_alergie,psychiatric_treatment,medication,doctor_name,doctor_phone,observations):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(os.environ.get('DEFAULT_FROM_EMAIL'))
        to_email = Email(os.environ.get('DEFAULT_TO_EMAIL'))
        subject = "Formulário de saúde - Drubchen de Khadro Sangdu"
        sendgrid_content = Content("text", 'DADOS PESSOAIS' + '\n' + '\n' +
                                    'Nome: ' + name + '\n' + '\n'
                                    'E-mail: ' + email + '\n' + '\n' +
                                    'Data de nascimento: ' + birthday_br + '\n' + '\n' + '\n' +

                                    'CONVÊNIO MÉDICO' + '\n' + '\n' +

                                    'Convênio: ' + medical_agreement + '\n' + '\n' +
                                    'Cobertura: ' + coverage + '\n' + '\n' +
                                    'Telefone: ' + phone + '\n' + '\n' +

                                    'CONTATO DE EMERGÊNCIA' + '\n' + '\n' +
                                    'Nome: ' + emergency_contact_name + '\n' + '\n' +
                                    'Parentesco: ' + emergency_contact_degree + '\n' + '\n' +
                                    'Telefone: ' + emergency_contact_phone + '\n' + '\n' +
                                    'Email: ' + emergency_contact_email + '\n' + '\n' +

                                    'HISTÓRICO MÉDICO' + '\n' + '\n' +
                                    'Problema de saúde: ' + health_problems + '\n' + '\n' +
                                    'Alergia a:' + '\n' +
                                    'Medicamentos: ' + medicines_alergie + '\n' +
                                    'Comida: ' + food_alergie + '\n' +
                                    'Alergia ' + insect_alergie + '\n' + '\n' +
                                    'Tratamento psiquiátrico ou psicológico: ' + psychiatric_treatment + '\n' + '\n' +
                                    'Usa medicação: ' + medication + '\n' + '\n' +
                                    'Algum médico que acompanha a sua saúde?' + '\n' +
                                    'Nome: ' + doctor_name + '\n' + '\n' +
                                    'Telefone: ' + doctor_phone + '\n' + '\n' +
                                    'Observações: ' + observations + '\n' + '\n'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
