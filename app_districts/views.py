from django.views.generic import ListView
from django.http import HttpResponse
from django.db.models import F
from django.shortcuts import render
from .models import Districts

class DistrictsListView(ListView):
    model = Districts
    template_name = "index.html"
    context_object_name = "districts"

    def get_queryset(self):
        lang = self.request.session.get("lang", "uz")
        queryset = (
            Districts.objects.all()
            .values("district_name_" + lang)
            .annotate(district_name=F("district_name_" + lang))
        )
        return queryset

def setLanguage(request, lang):
    try:
        request.session["lang"] = lang
        return HttpResponse("ok")
    except Exception as e:
        return HttpResponse(f"error: {str(e)}")
