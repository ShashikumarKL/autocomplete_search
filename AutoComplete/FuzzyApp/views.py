from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class indexpage(TemplateView):
	def get(self,request,**kwargs):
		return render(request,'index.html',context=None)


class displaypage(TemplateView):
	def get(self,request,**kwargs):
		self.search=request.GET['search']
        
		return render(request,'display.html',{"search_text":self.search,"some":"shashikmmfmamr"})

