from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework.validators import UniqueTogetherValidator



class UserSerializer(serializers.ModelSerializer):
    """
    serializer for creating user object
    """
    email = serializers.EmailField(required=True,allow_blank=False,allow_null=False,
                                   validators=[UniqueValidator(queryset=User.objects.all(),
                                                               message="email already exists!",
                                                               lookup='exact')])
    username = serializers.CharField(required=True,allow_blank=False,allow_null=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message="username is taken!,try another",
                                                                 lookup='exact')])
    password = serializers.CharField(style={'input_type': 'password'},required=True,
                                     allow_blank=False,allow_null=False)
    confirm_password = serializers.CharField(style={'input_type':'password'},required=True)

    class Meta:
        model = User
        fields = ('id','username', 'email','password','confirm_password')

    def validate(self, data):

        """
        function for password validation
        :param data:
        :return:
        """
        password = data.get('password')
        pass_cnf = data.get('confirm_password')

        if password != pass_cnf:
               raise ValidationError("Password didn't matched ")
        if len(password) < 6:
               raise ValidationError("password of minimum 6 digit is required")
        else:
            return data


class OTPSerializer(serializers.ModelSerializer):
    """
    serializer for otp
    """

    class Meta:
        model = OTP
        fields = ['otp']

class LoginSerializer(serializers.ModelSerializer):
    """
    login serializer
    """

    uname_or_em = serializers.CharField(allow_null=False,required=True)
    password = serializers.CharField(style={'input_type': 'password'},required=True,
                                     allow_blank=False,allow_null=False)

    class Meta:
        model = User
        fields = ('uname_or_em','password')


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields= '__all__'

class DeliveryAddressSerializer(serializers.ModelSerializer):
    """
    serializer for delivery address
    """

    class Meta:
        model = DeliveryAddress
        fields = '__all__'
        read_only_fields = ('user',)


class PickupAddressSerializer(serializers.ModelSerializer):
    """
    serializer for pickup address
     """
    class Meta:
        model = PickupAddress
        fields = '__all__'
        read_only_fields = ('user',)

class SellerDetailsSerializer(serializers.ModelSerializer):

    """
    serializer for seller detail
    """

    class Meta:
        model = SellerDetails
        fields = '__all__'
        read_only_fields= ('user',)


