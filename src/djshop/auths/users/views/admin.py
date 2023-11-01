from rest_framework.authtoken.views import ObtainAuthToken

from djshop.auths.users.serializers.admin import UserAdminSerializer


class AdminLoginView(ObtainAuthToken):

    serializer_class = UserAdminSerializer