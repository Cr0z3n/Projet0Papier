
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .calendrier import Calendar
import calendar
from django.urls import reverse
from django.shortcuts import  get_object_or_404
from .forms import *
from django.shortcuts import redirect


from django.contrib.auth.decorators import login_required
from user.views import group_required



class CalendarView(generic.ListView):
	model = Event
	template_name = 'planning/calendar.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

        # use today's date for the calendar
		d = get_date(self.request.GET.get('month', None))
		user = self.request.user


        # Instantiate our calendar class with today's year and date
		cal = Calendar(d.year, d.month,user)

        # Call the formatmonth method, which returns our calendar as a table
		html_cal = cal.formatmonth(withyear=True)
		context['calendar'] = mark_safe(html_cal)
		d = get_date(self.request.GET.get('month', None))
		context['prev_month'] = prev_month(d)
		context['next_month'] = next_month(d)
		return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

# ici mettre une permission que seul le responsable de parcours puisse modifier l'event pas uniquement login_required
@group_required('Responsables de parcours')
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('planning:calendar'))
    return render(request, 'planning/event.html', {'form': form})