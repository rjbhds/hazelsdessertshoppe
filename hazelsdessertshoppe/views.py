
from django.views.generic import TemplateView, FormView
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from hazelsdessertshoppe.config import CONFIG_CONTEXT
from hazelsdessertshoppe.forms import ProductForm
from hazelsdessertshoppe.file_upload import resize_image, create_image_version

MENU_COMMAND_TITLES = {
    'bycategory': 'By Category',
    'default': 'Alphabetical',
    'pies': 'Pies',
    'cookies': 'Cookies',
    'cakes': 'Cakes',
    'bread': 'Bread'
}
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

        context = super().get_context_data(**kwargs)

        context['is_home_page'] = True

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

class About(BasePage, TemplateView):
    template_name = 'about.html'
    page_header = None
    page_header_byline = None
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context

class Menu(BasePage, TemplateView):
    template_name = 'menu.html'
    page_header = None
    page_header_byline = None
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        command = self.kwargs.get('command') or 'command'

        context['category_title'] = MENU_COMMAND_TITLES.get(command, MENU_COMMAND_TITLES['default'])
        
        return context

class MenuAdd(BasePage, FormView):
    template_name = 'menu_add.html'
    page_header = None
    page_header_byline = None
    success_message = "Product was successfully added!"

    form_class = ProductForm
    
    def post(self, request, *args, **kwargs):

#         if 'file' in request.FILES:
#             print("request.FILES['file'] = {}".format(request.FILES['file'].name))
#             print("request.FILES['file'] = {}".format(request.FILES['file'].size))
        
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
#             if 'file' in request.FILES:
#                 handle_uploaded_file(request.FILES['file'])
            
#             print(form.instance.image.url)
            resize_image(form.instance.image.url)
            create_image_version(form.instance.image.url, 'profile')
            create_image_version(form.instance.image.url, 'thumb')

            messages.success(request, self.success_message)

            print(request.resolver_match.url_name)
            
            return redirect(request.resolver_match.url_name)
        
#             return render_to_response(
#                 self.template_name,
#                 context_instance=RequestContext(
#                     request,
#                     self.get_context_data(form=self.form_class)
#                 )
#             )
        else:
            
            return render_to_response(
                self.template_name,
                context_instance=RequestContext(
                    request,
                    self.get_context_data(form=self.form_class)
                )
            )

        return self.get(request, args, kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context

class Error404(BasePage, TemplateView):
    template_name = '404.html'
    page_header = None
    page_header_byline = None

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['last_good_url'] = self.request.session.get('last_good_url')
        
        return context
