import sendgrid
import os
from sendgrid.helpers.mail import *
# import pdb; pdb.set_trace()
import re



def sendMail(name,birthday,adress,adress_num,adress_comp,city,state,country,zip_code,email,phone,gender,initiations,initiations_lama,monastic_ordenation,observations,food_preferency,seat,payment, payment_international,payment_info,event_option):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(email)
        to_email = Email(os.environ.get('DEFAULT_TO_EMAIL'))
        subject = "Formulário de inscrição - Drubchen de Khadro Sangdu"
        sendgrid_content = Content("text/html", '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title></title><style media="screen">ul {font-size: 1.3em;}li {margin-bottom: 20px;}</style></head><body><h2>Dados Pessoais</h2><ul><li>Nome: ' + name +
                                        '</li><li>Data de nascimento: ' + birthday +
                                        '</li><li>Endereço: ' + adress +
                                        '</li><li>Número: ' + adress_num +
                                        '</li><li>Complemento: ' + adress_comp +
                                        '</li><li>Cidade: ' + city +
                                        '</li><li>Estado: ' + state +
                                        '</li><li>País: ' + country +
                                        '</li><li>CEP: ' + zip_code +
                                        '</li><li>E-mail: ' + email +
                                        '</li><li>Telefone/celular: ' + phone +
                                        '</li><li>Gênero: ' + gender +
                                        '</li><li>Iniciações: ' + initiations +
                                        '</li><li>Professores que concederam as iniciações: ' + initiations_lama +
                                        '</li><li>Ordenação monástica: ' + monastic_ordenation +
                                        '</li><li>Observações gerais: ' + observations +
                                        '</li><li>Preferência alimentar: ' + food_preferency +
                                        '</li><li>Necessidade de cadeira: ' + seat +
                                        '</li><li>Opção de evento: ' + event_option +
                                        '</li><li>Forma de pagamento: ' + payment + payment_international +
                                        '</li><li>Dados do pagamento: ' + payment_info +
                                        '</li></ul></body></html>'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)

def sendMailError(name,birthday_br,adress,adress_num,adress_comp,city,state,country,zip_code,email,phone,gender,initiations,initiations_lama,monastic_ordenation,observations,food_preferency,seat,payment, payment_international,payment_info,event_option):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(email)
        to_email = Email('davidbarenco@gmail.com')
        subject = "Error: incrição - " + name
        sendgrid_content = Content("text/html", '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title></title><style media="screen">ul {font-size: 1.3em;}li {margin-bottom: 20px;}</style></head><body><h2>Dados Pessoais</h2><ul><li>Nome: ' + name +
                                        '</li><li>Data de nascimento: ' + birthday_br +
                                        '</li><li>Endereço: ' + adress +
                                        '</li><li>Número: ' + adress_num +
                                        '</li><li>Complemento: ' + adress_comp +
                                        '</li><li>Cidade: ' + city +
                                        '</li><li>Estado: ' + state +
                                        '</li><li>País: ' + country +
                                        '</li><li>CEP: ' + zip_code +
                                        '</li><li>E-mail: ' + email +
                                        '</li><li>Telefone/celular: ' + phone +
                                        '</li><li>Gênero: ' + gender +
                                        '</li><li>Iniciações: ' + initiations +
                                        '</li><li>Professores que concederam as iniciações: ' + initiations_lama +
                                        '</li><li>Ordenação monástica: ' + monastic_ordenation +
                                        '</li><li>Observações gerais: ' + observations +
                                        '</li><li>Preferência alimentar: ' + food_preferency +
                                        '</li><li>Necessidade de cadeira: ' + seat +
                                        '</li><li>Opção de evento: ' + event_option +
                                        '</li><li>Forma de pagamento: ' + payment + payment_international +
                                        '</li><li>Dados do pagamento: ' + payment_info +
                                        '</li></ul></body></html>'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)


def sendMailHealth(name,email,birthday,medical_agreement,coverage,phone,emergency_contact_name,emergency_contact_degree,emergency_contact_phone, emergency_contact_email,health_problems,medicines_alergie,food_alergie,insect_alergie,psychiatric_treatment,medication,doctor_name,doctor_phone,observations):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(email)
        to_email = Email(os.environ.get('DEFAULT_TO_EMAIL'))
        subject = "Formulário de saúde - " + name
        sendgrid_content = Content("text/html", '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title></title><style media="screen">ul {font-size: 1.3em;}li {margin-bottom: 20px;}</style></head><body><h1>FICHA DE SAÚDE</h1><h2>Dados Pessoais</h2><ul><li>Nome: ' + name +
                                        '</li><li>E-mail: ' + email +
                                        '</li><li>Data de nascimento: ' + birthday +
                                        '</li><h2>Convênio Médico</h2><li>Convênio: ' + medical_agreement +
                                        '</li><li>Cobertura: ' + coverage +
                                        '</li><li>Telefone: ' + phone +
                                        '</li><h2>Contato de emergência</h2><li>Nome: ' + emergency_contact_name +
                                        '</li><li>Parentesco: ' + emergency_contact_degree +
                                        '</li><li>Telefone: ' + emergency_contact_phone +
                                        '</li><li>Email: ' + emergency_contact_email +
                                        '</li><h2>Histórico médico</h2><li>Problema de saúde: ' + health_problems +
                                        '</li><p>Alergia a:</p><li>Medicamentos: ' + medicines_alergie +
                                        '</li><li>Comida: ' + food_alergie +
                                        '</li><li>Insetos: ' + insect_alergie +
                                        '</li><li>Tratamento psiquiátrico ou psicológico: ' + psychiatric_treatment +
                                        '</li><li>Usa medicação: ' + medication +
                                        '</li><p>Algum médico que acompanha a sua saúde?</p><li>Nome: ' + doctor_name +
                                        '</li><li>Telefone: ' + doctor_phone +
                                        '</li><li>Observações: ' + observations +
                                        '</li></ul></body></html>'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
def sendMailHealthError(name,email,birthday,medical_agreement,coverage,phone,emergency_contact_name,emergency_contact_degree,emergency_contact_phone, emergency_contact_email,health_problems,medicines_alergie,food_alergie,insect_alergie,psychiatric_treatment,medication,doctor_name,doctor_phone,observations):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(email)
        to_email = Email('davidbarenco@gmail.com')
        subject = "Error: saúde - " + name
        sendgrid_content = Content("text/html", '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title></title><style media="screen">ul {font-size: 1.3em;}li {margin-bottom: 20px;}</style></head><body><h1>FICHA DE SAÚDE</h1><h2>Dados Pessoais</h2><ul><li>Nome: ' + name +
                                        '</li><li>E-mail: ' + email +
                                        '</li><li>Data de nascimento: ' + birthday +
                                        '</li><h2>Convênio Médico</h2><li>Convênio: ' + medical_agreement +
                                        '</li><li>Cobertura: ' + coverage +
                                        '</li><li>Telefone: ' + phone +
                                        '</li><h2>Contato de emergência</h2><li>Nome: ' + emergency_contact_name +
                                        '</li><li>Parentesco: ' + emergency_contact_degree +
                                        '</li><li>Telefone: ' + emergency_contact_phone +
                                        '</li><li>Email: ' + emergency_contact_email +
                                        '</li><h2>Histórico médico</h2><li>Problema de saúde: ' + health_problems +
                                        '</li><p>Alergia a:</p><li>Medicamentos: ' + medicines_alergie +
                                        '</li><li>Comida: ' + food_alergie +
                                        '</li><li>Insetos: ' + insect_alergie +
                                        '</li><li>Tratamento psiquiátrico ou psicológico: ' + psychiatric_treatment +
                                        '</li><li>Usa medicação: ' + medication +
                                        '</li><p>Algum médico que acompanha a sua saúde?</p><li>Nome: ' + doctor_name +
                                        '</li><li>Telefone: ' + doctor_phone +
                                        '</li><li>Observações: ' + observations +
                                        '</li></ul></body></html>'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)

def sendMailVolunteer(name, birthday, adress, adress_num, adress_comp,city, state, country, zip_code, email, phone, gender, initiations, initiations_lama, monastic_ordenation, observations, food_preferency, seat, physical_problems, joint_problems, health_problems, payment, payment_international, payment_info, event_option):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(email)
        to_email = Email(os.environ.get('DEFAULT_TO_EMAIL'))
        subject = "Formulário de inscrição - Drubchen de Khadro Sangdu"
        sendgrid_content = Content("text/html", '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title></title><style media="screen">ul {font-size: 1.3em;}li {margin-bottom: 20px;}</style></head><body><h2>Dados Pessoais</h2><ul><li>Nome: ' + name +
                                        '</li><li>Data de nascimento: ' + birthday +
                                        '</li><li>Endereço: ' + adress +
                                        '</li><li>Número: ' + adress_num +
                                        '</li><li>Complemento: ' + adress_comp +
                                        '</li><li>Cidade: ' + city +
                                        '</li><li>Estado: ' + state +
                                        '</li><li>País: ' + country +
                                        '</li><li>CEP: ' + zip_code +
                                        '</li><li>E-mail: ' + email +
                                        '</li><li>Telefone/celular: ' + phone +
                                        '</li><li>Gênero: ' + gender +
                                        '</li><li>Iniciações: ' + initiations +
                                        '</li><li>Professores que concederam as iniciações: ' + initiations_lama +
                                        '</li><li>Ordenação monástica: ' + monastic_ordenation +
                                        '</li><li>Observações gerais: ' + observations +
                                        '</li><li>Preferência alimentar: ' + food_preferency +
                                        '</li><li>Necessidade de cadeira: ' + seat +
                                        '</li><li>Problema físico que impeça de carregar peso: ' + physical_problems +
                                        '</li><li>Problema articular: ' + joint_problems +
                                        '</li><li>Problema de saúde que cause limitação para atividades físicas ou para algum função: ' + health_problems +
                                        '</li><li>Opção de evento: ' + event_option +
                                        '</li><li>Forma de pagamento: ' + payment + payment_international +
                                        '</li><li>Dados do pagamento: ' + payment_info +
                                        '</li></ul></body></html>'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)

def sendMailVolunteerError(name, birthday, adress, adress_num, adress_comp,city, state, country, zip_code, email, phone, gender, initiations, initiations_lama, monastic_ordenation, observations, food_preferency, seat, physical_problems, joint_problems, health_problems, payment, payment_international, payment_info, event_option):
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('DKR_SG_API_KEY'))
        from_email = Email(email)
        to_email = Email(os.environ.get('DEFAULT_TO_EMAIL'))
        subject = "Formulário de inscrição - Drubchen de Khadro Sangdu"
        sendgrid_content = Content("text/html", '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title></title><style media="screen">ul {font-size: 1.3em;}li {margin-bottom: 20px;}</style></head><body><h2>Dados Pessoais</h2><ul><li>Nome: ' + name +
                                        '</li><li>Data de nascimento: ' + birthday +
                                        '</li><li>Endereço: ' + adress +
                                        '</li><li>Número: ' + adress_num +
                                        '</li><li>Complemento: ' + adress_comp +
                                        '</li><li>Cidade: ' + city +
                                        '</li><li>Estado: ' + state +
                                        '</li><li>País: ' + country +
                                        '</li><li>CEP: ' + zip_code +
                                        '</li><li>E-mail: ' + email +
                                        '</li><li>Telefone/celular: ' + phone +
                                        '</li><li>Gênero: ' + gender +
                                        '</li><li>Iniciações: ' + initiations +
                                        '</li><li>Professores que concederam as iniciações: ' + initiations_lama +
                                        '</li><li>Ordenação monástica: ' + monastic_ordenation +
                                        '</li><li>Observações gerais: ' + observations +
                                        '</li><li>Preferência alimentar: ' + food_preferency +
                                        '</li><li>Necessidade de cadeira: ' + seat +
                                        '</li><li>Problema físico que impeça de carregar peso: ' + physical_problems +
                                        '</li><li>Problema articular: ' + joint_problems +
                                        '</li><li>Problema de saúde que cause limitação para atividades físicas ou para algum função: ' + health_problems +
                                        '</li><li>Opção de evento: ' + event_option +
                                        '</li><li>Forma de pagamento: ' + payment + payment_international +
                                        '</li><li>Dados do pagamento: ' + payment_info +
                                        '</li></ul></body></html>'
                                    )


        mail = Mail(from_email, subject, to_email, sendgrid_content)

        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
