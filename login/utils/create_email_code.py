import datetime

from login import models
from login.utils.salt import hash_code


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user, now)
    models.ConfirmString.objects.create(code=code, user=user)
    return code