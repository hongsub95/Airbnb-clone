from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


"""
#FBV(Function Based)

def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()

"""


class RoomDetail(DetailView):

    model = models.Room


def search(request):
    city = request.GET.get("city", "AnyWhere")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
