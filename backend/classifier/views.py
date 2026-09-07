from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def predict(request):

    # Test GET request
    if request.method == 'GET':
        return Response({
            "message": "Image classifier API is working!"
        })

    # POST request
    if 'image' not in request.FILES:
        return Response(
            {"error": "No image uploaded."},
            status=400
        )

    image = request.FILES['image']

    print("Image received:", image.name)

    # Temporary response
    return Response({
        "predictions": [
            {
                "label": "Test Image",
                "confidence": 95
            }
        ]
    })