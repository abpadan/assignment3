from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from .models import Tool, Available
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import requests


class ToolListView(LoginRequiredMixin, ListView):
    model = Tool
    template_name = 'tools_list.html'


class ToolCreateView(LoginRequiredMixin, CreateView):
    model = Tool
    template_name = 'tools_new.html'
    fields = ('name', 'manufacturer', 'notes', 'available', 'type')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ToolEditView(LoginRequiredMixin, UpdateView):
    model = Tool
    fields = ('name', 'manufacturer', 'notes', 'available', 'type', 'requested')
    template_name = 'tools_edit.html'


class ToolDeleteView(LoginRequiredMixin, DeleteView):
    model = Tool
    template_name = 'tools_delete.html'
    success_url = reverse_lazy('tools_list')


def send_email(tool_id, owner_email, logged_in_user_email):
    domain = "****"
    api_key = "****"

    requests.post(
        "https://api.mailgun.net/v3/" + domain + "/messages",
        auth=("api", api_key),
        data={"from": "Mailgun User <mailgun@" + domain + ">",
              "to": [owner_email],
              "subject": "Tool is being requested by user " + logged_in_user_email,
              "text": "Tool with id= " + tool_id + " is being requested by user " + logged_in_user_email},
        verify=False)

    requests.post(
        "https://api.mailgun.net/v3/" + domain + "/messages",
        auth=("api", api_key),
        data={"from": "Mailgun User <mailgun@" + domain + ">",
              "to": [logged_in_user_email],
              "subject": "Tool request sent",
              "text": "Tool request sent for tool with id=" + tool_id + " to owner " + owner_email},
        verify=False)


class ToolRequestView(LoginRequiredMixin, UpdateView):
    model = Tool
    fields = ('requested',)
    template_name = 'tools_request.html'
    success_url = reverse_lazy('tools_list')

    def form_valid(self, form):
        tool_id = str(self.get_object().id)
        owner_email = str(self.get_object().owner.email)
        logged_in_user_email = str(self.request.user.email)
        send_email(tool_id, owner_email, logged_in_user_email)
        form.save()
        return HttpResponseRedirect(self.get_success_url())
