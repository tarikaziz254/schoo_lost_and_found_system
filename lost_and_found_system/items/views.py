from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ReportItemForm
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'items/item_list.html'
    context_object_name = 'items'
    ordering = ['-date_lost_or_found']

class ItemCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/post_item.html'
    success_url = reverse_lazy('item-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Item
    fields = ['status']  # Only allowing the status to be updated
    template_name = 'report_item_update.html'
    
    def form_valid(self, form):
        item = form.save(commit=False)
        
        # Check if the item is marked as 'picked'
        if item.status == 'picked':
            item.delete()  # Automatically delete the item when picked
            return redirect(reverse_lazy('item-list'))  # Redirect after deletion
        
        # Otherwise, just save the item with the updated status
        item.save()
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff



class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'items/item_delete.html'
    success_url = reverse_lazy('item-list')
    

    def test_func(self):
        # Only staff or superuser can delete
        if self.request.user.is_staff or self.request.user.is_superuser:
            return True
        raise PermissionDenied()
    

class ItemReportView(LoginRequiredMixin,CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/report_item.html'
    success_url = reverse_lazy('item-list')

    def form_valid(self, form):
        # Ensure the logged-in user is assigned to the item
        form.instance.user = self.request.user
        return super().form_valid(form)

from django.views.generic import FormView
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

class ContactStaffView(FormView):
    template_name = 'items/contact_staff.html'  # The template to render
    form_class = ContactForm  # The form to use
    success_url = reverse_lazy('contact-success')  # Redirect to a success page upon successful form submission

    def form_valid(self, form):
        # Get the form data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        phone_number = form.cleaned_data['phone_number']
        whatsapp_number = form.cleaned_data['whatsapp_number']
        
        # Send an email with the form data
        send_mail(
            f"Message from {name}",
            f"Email: {email}\nPhone: {phone_number}\nWhatsApp: {whatsapp_number}\nMessage: {message}",
            email,
            ['staff@example.com'],  # Replace with the actual staff email
        )
        
        return super().form_valid(form)