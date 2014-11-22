from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, RedirectView, CreateView, ListView

from apps.tracking.models import Link
from tracking.forms import CreateLinkForm
from utils.base_62_converter import saturate
from utils.helpers import reverse_absolute_uri, get_remote_addr


class RedirectLinkView(RedirectView):
    link_object = None

    def get(self, request, *args, **kwargs):
        self.link_object = self.get_link_object()
        if self.link_object:
            self.link_object.logs.create(ip_address=get_remote_addr(self.request),
                                         referrer=self.request.META.get('HTTP_REFERER'))
            return HttpResponseRedirect(self.link_object.url)
        else:
            super(RedirectLinkView, self).get(request, *args, **kwargs)

    def get_link_object(self):
        link_id = saturate(self.kwargs.get('b62_key'))
        try:
            return Link.objects.get(pk=link_id)
        except Link.DoesNotExist:
            return None


class LinkCreateView(CreateView):
    form_class = CreateLinkForm
    template_name = 'tracking/link_form.html'

    def get_success_url(self):
        return reverse_lazy('tracking:detail', args=(self.object.slug, ))


class LinkListView(ListView):
    model = Link
    template_name = 'tracking/link_list.html'


class LinkDetailView(DetailView):
    model = Link
    template_name = 'tracking/link_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LinkDetailView, self).get_context_data(**kwargs)
        context['short_url'] = reverse_absolute_uri(self.request, 'redirect_link',
                                                    kwargs={'b62_key': saturate(self.object.slug)})
        return context