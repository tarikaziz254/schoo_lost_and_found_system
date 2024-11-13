from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ItemListView(ListView):
    model = Item
    template_name = 'items/item_list.html'
    context_object_name = 'items'
    ordering = ['-date_lost_or_found']

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/post_item.html'
    success_url = reverse_lazy('item-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/update_item.html'
    success_url = reverse_lazy('item-list')

    def test_func(self):
        return self.request.user.is_staff

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'items/delete_item.html'
    success_url = reverse_lazy('item-list')

    def test_func(self):
        item = self.get_object()
        return self.request.user == item.user and item.collected

