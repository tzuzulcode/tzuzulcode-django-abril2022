from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

# Create your models here.
class EmailBackEnd(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):

        User = get_user_model()

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None