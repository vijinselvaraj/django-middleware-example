from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
# Create your views here.
class Index(CreateView):
	def get(self, request, *args, **kwargs):
		try:
			name = self.request.name
		except Exception as e:
			print(e)
			name = "middleware not loadded"
			
		return render(request, "index.html", {'name':name})