from mkt.models import Ad
from mkt.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad
    template_name = 'mkt/ad_list.html'


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'mkt/ad_detail.html'


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = 'mkt/ad_form.html'


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = 'mkt/ad_form.html'


class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'mkt/ad_confirm_delete.html'
