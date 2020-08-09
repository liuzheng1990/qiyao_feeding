from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from . models import QiyaoEvent

def index(request):
    return render(request, "qiyao_events/index.html")

class EventListView(ListView):
    model = QiyaoEvent
    def get_queryset(self):
        return QiyaoEvent.objects.order_by("time").all()[:10]


class EventAddView(CreateView):
    model = QiyaoEvent
    fields = ['event_type', 'time', 'int_param', 'str_param']
    success_url = reverse_lazy('events-list')


class EventUpdateView(UpdateView):
    model = QiyaoEvent
    fields = ['event_type', 'time', 'int_param', 'str_param']
    success_url = reverse_lazy('events-list')


class EventDeleteView(DeleteView):
    model = QiyaoEvent
    success_url = reverse_lazy('events-list')
    