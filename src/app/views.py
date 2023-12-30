import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from serializers.user_endpoint_serialzers import AddUserSerializer, LoginUserSerializer
from django.contrib.auth.hashers import make_password
from.swagger import AddUserXcodeAutoSchema, LoginUserXcodeAutoSchema
from . import settings
from django.db.models import Q

class AppPages:
    @classmethod
    def home(cls,request):
        """
        Render the home pae
        :param request:
        :return:
        """
        return render(request, 'home.html', {'name': 'Habib', 'title' : "Pay  Space Home"})

    @classmethod
    def login(cls, request):
        """
        Render the home pae
        :param request:
        :return:
        """
        return render(request, 'login.html', {'expires': settings.EXPIRES_Days, 'title': "Login to Pay Space"})

    @classmethod
    def sign_up(cls, request):
        """
        Render the home pae
        :param request:
        :return:
        """
        return render(request, 'sign-up.html', {'name': 'Habib', 'title': "Sign-Up"})


class UserManagement(viewsets.ViewSet):

    def __user_exists(self,username=None, email=None):
        """
        Inner function check if the user exists

        :param username: Username to check
        :param email: Email to check
        :return: Returns True or False
        ":rtype: bool
        """
        user_exists = email_exists = False
        if username is not None:
            user_exists = User.objects.filter(username=username).exists()
        if email is not None:
            email_exists = User.objects.filter(email=email).exists()

        return user_exists and email_exists
    @method_decorator(
        decorator=swagger_auto_schema(
            operation_summary="Add a user to the list of app users",
            operation_description="""
            Create a user in the database based on the Users Model

            Parameters:
            -----------

            - **request** (`HttpRequest`): Here is the list of parameters:
                - `username` : User name
                - `password` : Password of the user
                - `email` : Email of the user
                - `first_name` : First name of the user
                - `last_name` : Last name of the user

            Returns:
            --------

            - **`HttpResponse`**: Return the response code with its content
            """,
            responses=AddUserXcodeAutoSchema.responses(),
            auto_schema=AddUserXcodeAutoSchema,
            tags=['User Endpoints']
        )
    )
    @action(methods=['post'],
            detail=False,
            url_path='add_none_admin_user',
            permission_classes=[AllowAny,])
    def add_none_admin_user(self,request):


        serializer = AddUserSerializer(data=request.data)

        """
        Check if the data is validate
        """
        if serializer.is_valid():
            """
            Check if the user exists in the database
            """
            if not (self.__user_exists(username=serializer.validated_data['username'],
                                  email=serializer.validated_data['email'])):
                """
                Add the user
                """
                new_user = User(
                    username=serializer.validated_data['username'],
                    email=serializer.validated_data['email'],
                    first_name=serializer.validated_data['first_name'],
                    last_name=serializer.validated_data['last_name'],
                    password=make_password(serializer.validated_data['password'],
                                           salt=settings.DEFAULT_PASSWORD_SALT)
                )
                new_user.save()

                """
                Return the success message
                """
                response_data = {
                    "message": "User has been created successfully!!"
                }
                return Response(response_data, content_type="application/json", status=status.HTTP_201_CREATED)


            else:
                """
                Return user exists error
                """
                response_data = {
                    "error": "I found a user with the same username or email address",
                    "message": ""
                }
                return Response(response_data, content_type="application/json", status=status.HTTP_409_CONFLICT)

        else:
            """
            Rerun data validation error
            """
            response_data = {
                "error" : "The data is not validated. Please check the information you are sending to the endpoint.",
                "message": ""
            }
            return Response(response_data, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(
        decorator=swagger_auto_schema(
            operation_summary="Check user information for logging in the user",
            operation_description="""
                Check and login the user to the system

                Parameters:
                -----------

                - **request** (`HttpRequest`): Here is the list of parameters:
                    - `username` : User name
                    - `password` : Password of the user

                Returns:
                --------

                - **`HttpResponse`**: Return the response code with its content
                """,
            responses=LoginUserXcodeAutoSchema.responses(),
            auto_schema=AddUserXcodeAutoSchema,
            tags=['User Endpoints']
        )
    )
    @action(methods=['post'],
            detail=False,
            url_path='login_user',
            permission_classes=[AllowAny, ])
    def login_user(self, request):
        serializer = LoginUserSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']

            password = make_password(serializer.validated_data['password'],
                                     salt=settings.DEFAULT_PASSWORD_SALT)

            print(username, password)

            user_data = User.objects.filter(Q(username=username) &  Q(password=password))

            print(user_data)

            if user_data.exists() and bool(user_data.first().is_active):
                # return the user data
                response_data = {
                    "message" : "Login successful",
                    "user_data": {
                        "user_id" : user_data.first().id,
                        "username": user_data.first().username,
                        "email": user_data.first().email,
                        "first_name": user_data.first().first_name,
                        "last_name": user_data.first().last_name
                    }
                }
                return Response(response_data,
                                content_type="application/json",
                                status=status.HTTP_200_OK)
            elif user_data.exists() and not bool(user_data.first().is_active):
                response_data = {
                    "error": "The user is not active. Please contact system administrator",
                    "message": ""
                }
                return Response(response_data,
                                content_type="application/json",
                                status=status.HTTP_401_UNAUTHORIZED)
            else:
                response_data = {
                    "error": "Wrong username or password",
                    "message": ""
                }
                return Response(response_data,
                                content_type="application/json",
                                status=status.HTTP_401_UNAUTHORIZED)

        else:
            """
            Rerun data validation error
            """
            response_data = {
                "error" : "The data is not validated. Please check the information you are sending to the endpoint.",
                "message": ""
            }
            return Response(response_data, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)
