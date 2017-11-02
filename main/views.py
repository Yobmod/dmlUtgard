from django.shortcuts import render#, get_object_or_404, redirect
from django.conf import settings
#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader, Context, Template, RequestContext
from django.template.loader import render_to_string#, get_template
from django.views.generic import View
#from sekizai.context import SekizaiContext

def homepage(request):
	context = {}
	template_name = "main/homepage.html"
	if settings.DEBUG == True:
		if "/" in template_name and template_name.endswith('.html'):
			filename = template_name[(template_name.find("/")+1):len(template_name)-len(".html")] + "_flat.html"
		elif template_name.endswith('.html'):
			filename = template_name[:len(template_name)-len(".html")] + "_flat.html"
		else:
			raise ValueError("The template name could not be parsed or is in a subfolder")
		#print(filename)
		html_string = render_to_string(template_name, context, request=request)
		#print(html_string)
		filepath = "./templates_cdn/" + filename
		print(filepath)
		f = open(filepath, 'w+')
		f.write(html_string)
		f.close()
	return render(request, template_name, context)

def flatten(request):
	template_names = ["main/homepage.html", 'main/facilities.html']
	context = {}
	if settings.DEBUG == True:
		for template_name in template_names:
			if "/" in template_name and template_name.endswith('.html'):
				filename = template_name[(template_name.find("/")+1):len(template_name)-len(".html")] + "_flat.html"
			elif template_name.endswith('.html'):
				filename = template_name[:len(template_name)-len(".html")] + "_flat.html"
			else:
				raise ValueError("The template name could not be parsed or is in a subfolder")
			#print(filename)
			html_string = render_to_string(template_name, context)
			#print(html_string)
			filepath = "../templates_cdn/" + filename
			#print(filepath)
			f = open(filepath, 'w+')
			f.write(html_string)
			f.close()
			return render(request, template_name, context)



def render_to_file(template_name, context):
	html_string = render_to_string(template_name, context)
	#filename = template_name[:-5] + "_flat.html"
	#filename = template_name.replace('.html','_flat.html')
	#filename = template_name[:len(template_name)-len(".html")] + "_flat.html"
	#filename = template_name[:template_name.rfind(".")] + "_flat.html"
	#f = open(filename, 'w+')
	#f.write(html_string)
	#f.close()


# def webPageToText(url):
# 	import urllib2
# 	response = urllib2.urlopen(url)
# 	html = response.read()
# 	text = stripTags(html).lower()
# 	return text

def facilities(request):
	context = {}
	return render(request, 'main/facilities.html', context)

from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def projects(request):
	context = {}
	return render(request, 'main/projects.html', context)

def actinide_water_abs(request):
	context = {}
	return render(request, 'distinctive/_slides_base.html', context)

def publications(request):
	context = {}
	return render(request, 'main/publications.html', context)

def atoms(request):
	context = {}
	return render(request, 'animated_atoms.html', context)

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
