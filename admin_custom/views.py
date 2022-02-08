from django.views.generic.base import TemplateView

class AdminHomeView(TemplateView):
    template_name = 'admin/admin_home.html'