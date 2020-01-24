from django.shortcuts import render

def landing_page(request):
	number_of_fireflies = 42
	context = {
		'number_of_fireflies' : number_of_fireflies
	}
	return render(request, 'landing_page.html')