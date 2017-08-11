from django.shortcuts import render#, get_object_or_404, redirect
from django.conf import settings
#from django.http import HttpResponse
from django.views.generic import View


def homepage(request):
	#context = {}
	return render(request, 'main/homepage.html')#, context)

def facilities(request):
	context = {}
	return render(request, 'main/facilities.html', context)

def projects(request):
	context = {}
	return render(request, 'main/projects.html', context)

def publications(request):
	context = {}
	return render(request, 'main/publications.html', context)

def contact(request):
	# form = ContactForm(request.POST or None)
	# if form.is_valid():
	# 	form_name = form.cleaned_data.get('name')
	# 	form_email = form.cleaned_data.get('email')
	# 	form_message = form.cleaned_data.get('message')
	#
	# 	subject = 'Site contact form'
	# 	from_email = settings.EMAIL_HOST_USER
	# 	to_email = [from_email, 'other@email.com']
	# 	contact_message = "%s: %s via %s"%(form_name, form_message, form_email)
	# 	send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	#context = {'form':form,}
	context = {}
	return render(request, 'main/contact.html', context)


# @login_required
# def django_admin_page(request):
# 	return render(request, 'main/admin')
