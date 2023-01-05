import json

from django.http import JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad


@method_decorator(csrf_exempt, name='dispatch')
class AdListCreateView(View):

    def get(self, request):
        response = []
        for ad in Ad.objects.all():
            response.append({"id": ad.id,
                             "name": ad.name,
                             "author": ad.author,
                             "price": ad.price,
                             })
        return JsonResponse(response, safe=False)

    def post(self, request, **kwargs):
        data = json.loads(request.body)
        ad = Ad.objects.create(
            name=data["name"],
            author=data["author"],
            price=data["price"],
            description=data["description"],
            is_published=data["is_published"],
            address=data["address"],

        )
        return JsonResponse({"id": ad.id,
                             "name": ad.name,
                             "author": ad.author,
                             "price": ad.price,
                             "description": ad.description,
                             "is_published": ad.is_published}, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({"id": ad.id,
                             "name": ad.name,
                             "author": ad.author,
                             "price": ad.price,
                             "address": ad.address,
                             "description": ad.description,
                             "is_published": ad.is_published}, safe=False)
