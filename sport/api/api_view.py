from rest_framework.decorators import api_view
from rest_framework.response import Response

from sport.api.serializers import CategorySerializer
from sport.models import Category


@api_view(['GET'])
def get_categories(request):
    try:
        categories = Category.objects.all()
        ser = CategorySerializer(categories, many=True)
        data = {
            "success": True,
            "data": ser.data
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f'{err}'
        }
    return Response(data)
