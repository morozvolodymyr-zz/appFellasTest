import json

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

from appFellas.models import Image


@api_view(['GET'])
def get_images(request):
    if request.session.get('user_e_mail'):
        images = Image.objects.all()
        json_images = {'j_images': []}
        for image in images:
            name_format = image.image.name.split('.')
            name = name_format[0]
            form = name_format[1]
            temp = {'name': name,
                    'format': form,
                    'author': image.author.e_mail,
                    'uploaded': str(image.uploaded),
                    'link': image.image.url}
            json_images['j_images'].append(temp)
        return HttpResponse(json.dumps(json_images), content_type='application/json', status=status.HTTP_200_OK)
    else:
        images = Image.objects.all()
        json_images = {'j_images': []}
        for image in images:
            name_format = image.image.name.split('.')
            name = name_format[0]
            temp = {'name': name,
                    'format': None,
                    'author': None,
                    'uploaded': None,
                    'link': '/authorization'}
            json_images['j_images'].append(temp)
        return HttpResponse(json.dumps(json_images), content_type='application/json', status=status.HTTP_200_OK)