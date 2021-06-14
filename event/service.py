from event.models import Event
import time
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status


class ServiceEvents:
    """
    Service Class for Event
    Class to hold all the business logic for Models.
    Generic functions will go into Helper classes.
    """

    def addEvent(self, event_data):
        """
        Service method to add an event record
        :param event_data: Request body data to add an event
        :return:
        """
        try:
            create_event = Event()
            create_event.createdAt = int(time.time())
            create_event.email = event_data.get('email')
            create_event.message = event_data.get('message')
            create_event.component = event_data.get('component')
            create_event.environment = event_data.get('environment')
            create_event.data = event_data.get('data')
            create_event.save()

            return Response({
                'result': True,
                'value': 'Event has been created successfully.'
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'result': False,
                'value': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def getEvent(self, filter_data):
        """
        Service method to retrieve events.
        :param filter_data: filters to filter the QuerySet
        :return: filtered query set as JSON
        """
        try:
            filtered_events = Event.objects.all()
            filter_items = filter_data.items()

            filtered_events, filter_by_date = self.applyFilters(filter_items, filtered_events)

            if filter_by_date:
                # Process Only if created at filter is sent in the request body
                return self.applyDateFilter(filter_data, filtered_events)

            # Without filter by date field in request body
            return Response(filtered_events.values())
        except Exception as e:
            return Response({
                'result': False,
                'value': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def applyDateFilter(self, filter_data, filtered_events):
        """
        Apply date filter to filtered QuerySet
        :param filter_data:
        :param filtered_events:
        :return:
        """
        filter_date = datetime.strptime(filter_data.get('createdAt'), "%d-%m-%Y").date()
        filtered_events_by_date = []
        for event in filtered_events:
            if filter_date == event.get_created_date():
                eventdict = event.__dict__
                filtered_events_by_date.append({
                    "id": str(eventdict.get('id')),
                    "createdAt": eventdict.get('createdAt'),
                    "email": eventdict.get('email'),
                    "environment": eventdict.get('environment'),
                    "component": eventdict.get('component'),
                    "message": eventdict.get('message'),
                    "data": eventdict.get('data'),
                })
        return Response(filtered_events_by_date)

    def applyFilters(self, filter_items, filtered_events):
        """
        Apply all the field filters to QuerySet except date
        :param filter_items:
        :param filtered_events:
        :return:
        """
        filter_by_date = False
        for filter_field in filter_items:
            field = filter_field[0]
            value = filter_field[1]

            if field.lower() == "message":
                filtered_events = filtered_events.filter(**{field + '__' + 'icontains': value})
            elif field.lower() == "createdat":
                filter_by_date = True
            else:
                filtered_events = filtered_events.filter(**{field: value})

        return filtered_events, filter_by_date
