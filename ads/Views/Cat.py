import json

from django.http import JsonResponse


# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):

    def get(self, request):
        response = []
        for cat in Category.objects.all():
            response.append({"id": cat.id, "name": cat.name})
        return JsonResponse(response, safe=False)

    def post(self, request, **kwargs):
        data = json.loads(request.body)
        new_cat = Category.objects.create(
            name=data["name"]
        )
        return JsonResponse({"id": new_cat.id, "name": new_cat.name}, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({"id": cat.id, "name": cat.name}, safe=False)
