import random

import requests


def send_otp_to_phone(phone):
    try:
        #   Создание кода для подтверждения
        otp = random.randint(100000, 999999)
        #   Отправка кода, через SMS.RU
        url = f'https://sms.ru/sms/send?api_id={"Ваш API_ID"}&to={phone}&msg={otp}&json=1'
        response = requests.get(url)
        return otp

    except Exception:
        return None
