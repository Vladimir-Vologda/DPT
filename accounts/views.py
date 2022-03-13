from django.contrib.auth import get_user_model
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from accounts.sendler import send_otp_to_phone


User = get_user_model()


@api_view(['POST'])
def send_otp(request):
    data = request.data

    if data.get('phone') is None:
        return Response({
            'status': 400,
            'message': _('Phone number is required')
        })

    if data.get('name') is None:
        return Response({
            'status': 400,
            'message': _('Name is required')
        })

    if data.get('password1') is None:
        return Response({
            'status': 400,
            'message': _('Password is required')
        })

    if data.get('password2') is None:
        return Response({
            'status': 400,
            'message': _('Password confirmation is required')
        })
    #   Регистрация и отправка кода подтверждения
    user = User.objects.create(
        phone=data.get('phone'),
        name=data.get('name'),
        otp=send_otp_to_phone(data.get('phone')),
    )
    user.set_password = data.get('password')
    user.save()

    return Response({
        'status': 200,
        'message': 'Otp Sent',
    })


@api_view(['POST'])
def verified_otp(request):
    data = request.data

    if data.get('phone') is None:
        return Response({
            'status': 400,
            'message': _('Phone number is required')
        })

    if data.get('otp') is None:
        return Response({
            'status': 400,
            'message': _('Otp is required')
        })

    try:
        user_obj = User.objects.get(
            phone=data.get('phone'),
        )

    except Exception:
        return Response({
            'status': 400,
            'message': _('Invalid phone')
        })
    #   Подтверждение кода и получение статуса проверенный
    if user_obj.otp == data.get('otp'):
        user_obj.is_verified = True
        user_obj.save()
        return Response({
            'status': 200,
            'message': _('Otp successful')
        })

    return Response({
        'status': 400,
        'message': _('Invalid otp')
    })
