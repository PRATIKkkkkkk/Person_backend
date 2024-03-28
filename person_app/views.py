from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings


class PersonAPI(APIView):

    def get(self, request):
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many=True)
        return Response(data=serializer.data)
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            subject = 'Welcome Email'
            email = request.data.get('email')
            first_name = request.data.get('first_name')
            message = f'Thankyou for registring {first_name} Welcomme to the club!!!!!'
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                subject=subject,
                recipient_list=[email],
                message=message,
                from_email=from_email,fail_silently=False
            )
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    

class PersonDetailAPI(APIView):

    def get(self, request, pk):
        obj = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(obj)
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        obj = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(obj, data=request.data)
        if serializer.is_valid():
            subject = 'Update Email'
            email = obj.email
            first_name = obj.first_name
            message = f'Hey {first_name} You have successfully updated your data'
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                subject=subject,
                recipient_list=[email],
                message=message,
                from_email=from_email,fail_silently=False
            )
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def patch(self, request, pk):
        obj = get_object_or_404(Person, id=pk)
        serializer = PersonSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            subject = 'Update Email'
            email = obj.email
            first_name = obj.first_name
            message = f'Hey {first_name} You have successfully updated your data'
            from_email = settings.EMAIL_HOST_USER
            send_mail(
                subject=subject,
                recipient_list=[email],
                message=message,
                from_email=from_email,fail_silently=False
            )
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def delete(self, request, pk):
        obj = get_object_or_404(Person, id=pk)
        subject = 'Delete Email'
        email = obj.email
        first_name = obj.first_name
        message = f'{first_name} you just have deleted your account'
        from_email = settings.EMAIL_HOST_USER
        send_mail(
            subject=subject,
            recipient_list=[email],
            message=message,
            from_email=from_email,fail_silently=False
        )
        obj.delete()
        return Response(data=None)
    
