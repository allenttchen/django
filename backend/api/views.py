import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.models import Product
from product.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    #data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """django rest framework API"""
#     print(request.user)
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         #data = model_to_dict(model_data, fields=['id', 'title'])
#         data = ProductSerializer(instance).data
#     return Response(data)


# def api_home(request, *args, **kwargs):
#
#     print(request.GET) # URL Query params
#     print(request.POST)
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
