from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, get_default_timezone


def storage_information_view(request):
    unclosed_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for visit in unclosed_visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at, get_default_timezone()),
                'duration': visit.formatted_duration(),
            })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
