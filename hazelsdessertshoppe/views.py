
from django.views.generic import TemplateView, FormView
from hazelsdessertshoppe.config import CONFIG_CONTEXT

class BasePage(object):

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context.update(CONFIG_CONTEXT)
        
        return context

class HomePage(BasePage, TemplateView):
    template_name = 'home.html'
    page_header = None
    page_header_byline = None
    
    def get_context_data(self, **kwargs):
        self.request.session['current_app'] = 'hazelsdessertshoppe'
        self.request.session['next'] = '/'

        context = super().get_context_data(**kwargs)

        context['is_home_page'] = True
        context['next'] = '/'

        return context

class Login(TemplateView):
    template_name = 'home.html'
    page_header = None
    page_header_byline = None
    
    def get_context_data(self, **kwargs):
        self.request.session['current_app'] = 'hazelsdessertshoppe'
        self.request.session['next'] = '/'

        context = super().get_context_data(**kwargs)

        context['is_home_page'] = True
        context['next'] = '/'

        return context

