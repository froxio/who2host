from django.http import HttpResponse
from django.template import loader
from streamer.models import Streamer
from streamer.detail import get_streamer_info


def index(request):
    streamer_entries = len(Streamer.objects.all())
    less_popular_streamers = Streamer.objects.order_by('-stream_viewers')[
        streamer_entries//2:streamer_entries]
    context = {
        'less_popular_streamers': less_popular_streamers,
    }
    template = loader.get_template('streamer/index.html')
    return HttpResponse(template.render(context, request))


def detail(request, streamer_name):
    context = {
        'streamer_info': get_streamer_info(streamer_name),
    }
    template = loader.get_template('streamer/detail.html')
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('streamer/about.html')
    return HttpResponse(template.render(request))
