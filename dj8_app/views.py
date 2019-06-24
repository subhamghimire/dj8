from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request,'index.html')

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CBV=class based views")
# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'Basic Injection'
#         return context
class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'dj8_app/school_detail.html'
