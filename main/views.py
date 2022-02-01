from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	if request.method == "POST":
		cf_name = request.POST['cf-name']
		cf_lastname = request.POST['cf-lastname']
		cf_email = request.POST['cf-email']
		cf_subject = request.POST['cf-subject']
		cf_text = request.POST['cf-text']

        #send contact email

		send_mail(
			cf_name,
			cf_lastname,
			cf_email,
			['youremail@yahoo.com'],
			cf_subject,
			cf_text,
		)
		return render(request,'main/index.html', {'cf_name':cf_name})
	else:
		return render(request,'main/index.html')
