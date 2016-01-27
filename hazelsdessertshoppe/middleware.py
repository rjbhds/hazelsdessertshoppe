# Add logic here that should be processed for
# all views.
class MySessionProcessingMiddleware(object):

    # your desired cookie will be available in every HttpResponse parser like browser but not in django view
    def process_response(self, request, response):
        
        if hasattr(response, 'template_name'):
            if response.template_name:
                if not '404.html' in response.template_name:
                
                    request.session['last_good_url'] = request.build_absolute_uri()

        return response
