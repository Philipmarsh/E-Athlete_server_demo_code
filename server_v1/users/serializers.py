from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from .models import FCMToken

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'id', 'profile_photo',
                  'date_of_birth', 'sex', 'height', 'weight', 'sport', 'short_term_goal',
                  'medium_term_goal', 'long_term_goal']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    profile_photo = Base64ImageField(use_url=True)

class FCMTokenSerializer(serializers.ModelSerializer):

    # TODO fix this
    class Meta:
        model = FCMToken
        fields = ['token']
        # extra_kwargs = {
        #     'token': {'write_only': True}
        # }

