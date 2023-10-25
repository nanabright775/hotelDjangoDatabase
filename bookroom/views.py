from bookroom.models import BookRoom, Room
from bookroom.serializer import BookRoomSerializer, RoomSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


# from celery.schedules import crontab
# from django.http.response import HttpResponse
# from django.shortcuts import render
# from bookroom.tasks import send_mail_func
# from django_celery_beat.models import PeriodicTask, CrontabSchedule


# def send_mail_to_all(request):
#     send_mail_func.delay()
#     return HttpResponse("Sent")


# def schedule_mail(request):
#     schedule, created = CrontabSchedule.objects.get_or_create(minute=1)
#     task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_" +
#                                        "5", task='send_mail_app.tasks.send_mail_func')  # , args = json.dumps([[2,3]]))
#     return HttpResponse("Done")

class BookRoomView(viewsets.ModelViewSet):
    """views for booking room """
    serializer_class = BookRoomSerializer
    queryset = BookRoom.objects.all()
    def perform_create(self, serializer):
        # Check room availability before creating
        # data = self.request.data
        # check_in_date = data['check_in_date']
        # check_out_date = data['check_out_date']
        
        # if not is_room_available(check_in_date, check_out_date):
        #     return Response("Room is not available for the selected dates.", status=status.HTTP_400_BAD_REQUEST)
        
        print('mmamsamas')
        
        # serializer.save()
        
    # def perform_update(self, serializer):
    #     # Check room availability before updating
    #     instance = serializer.instance
    #     data = self.request.data
    #     check_in_date = data['check_in_date']
    #     check_out_date = data['check_out_date']
        
    #     if not is_room_available(check_in_date, check_out_date):
    #         return Response("Room is not available for the selected dates.", status=status.HTTP_400_BAD_REQUEST)
        
    #     serializer.save()

class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializers
    queryset = Room.objects.all()
    
    
def is_room_available(check_in_date, check_out_date, room_instance=None):
    # Add logic to check room availability based on start_date and end_date
    # You can use the room_instance to exclude the current room from the check
    pass