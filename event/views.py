from rest_framework.views import APIView
from .service import ServiceEvents


class EventView(APIView):
    """
    Event View - handle GET & POST requests.
    """

    def __init__(self):
        self.serviceHandler = ServiceEvents()

    def get(self, request):
        """
        Get event data - filtered by Event fields
        :param request:
        :return: Response
        """
        return self.serviceHandler.getEvent(request.data)

    def post(self, request):
        """
        Create event record with request data.
        :param request:
        :return: Response
        """
        return self.serviceHandler.addEvent(request.data)
