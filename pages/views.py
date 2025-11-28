from django.views.generic import TemplateView, ListView
from .models import Project
from blog.models import Post

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.filter(status='published')[:3]
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class PortfolioView(ListView):
    model = Project
    template_name = 'portfolio.html'
    context_object_name = 'projects'
