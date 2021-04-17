from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        # send an email
        send_mail(
            'Message from ' + message_name, # subject
            message, # message
            message_email, # from email
            ['pantufothought@gmail.com ', 'lurdes.l.paloma@gmail.com'], # To Email
        )
        return render(request, 'contact.html', {'message_name':message_name})
    else:
        return render(request, 'contact.html', {})

def offer(request):
    return render(request, 'offer.html', {})

def appointment(request):
    if request.method == 'POST':
        client_name = request.POST['client-name']
        client_phone = request.POST['client-phone']
        client_email = request.POST['client-email']
        client_address = request.POST['client-address']
        client_schedule = request.POST['client-schedule']
        client_date = request.POST['client-date']
        client_message = request.POST['client-message']

        # send an email
        appointment = f"""Name: {client_name} \tPhone: {client_phone} \tEmail: {client_email}
                        \tAddress: {client_address} \tShedule: {client_schedule} \tDate: {client_date}
                        \tMessage: {client_message}"""
        send_mail(
            'Appointment Request',  # subject
            appointment,  # client_message
            client_email,  # from email
            ['pantufothought@gmail.com ', 'lurdes.l.paloma@gmail.com'],  # To Email
        )
        return render(request, 'appointment.html', {
            'client_name': client_name,
            'client_phone': client_phone,
            'client_email': client_email,
            'client_address': client_address,
            'client_schedule': client_schedule,
            'client_date': client_date,
            'client_message': client_message
        })
    else:
        return render(request, 'appointment.html', {})

