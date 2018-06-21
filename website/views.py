from django.shortcuts import render
from website.forms import InscriptionForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

# Create your views here.
def index(request):
    form_class = InscriptionForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')

            template = get_template('form_template.txt')
            context = {
                'name': name,
                'email': email,
                'phone': phone,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': email }
            )
            email.send()
            return redirect('index')

    return render(request, 'base.html', {
        'form': form_class,
    })
