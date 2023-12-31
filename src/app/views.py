import json
from datetime import datetime

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
from serializers.address_endpoint_serializers import AddressRequestSerializer, AddressDetailRequestSerializer
from django.contrib.auth.hashers import make_password
from.swagger import (AddUserXcodeAutoSchema, LoginUserXcodeAutoSchema, GenerateAddressXcodeAutoSchema,
                     GenerateAddressListXcodeAutoSchema, GetAddressDetialsXcodeAutoSchema)
from utils.blockchain import BlockChain
from . import settings
from . import models
from django.db.models import Q, QuerySet


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

    @classmethod
    def addresses(cls, request):
        """
        Render the home pae
        :param request:
        :return:
        """
        return render(request, 'addresses.html', {'name': 'Habib', 'title': "Addresses"})


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


class AddressManagement(viewsets.ViewSet):
    """
    Endpoints for address management
    """

    @method_decorator(
        decorator=swagger_auto_schema(
            operation_summary="Generate a address for the user",
            operation_description="""
                    generate a address for the user

                    Parameters:
                    -----------

                    - **request** (`HttpRequest`): Here is the list of parameters:
                        - `user_id` : User ID requesting the address

                    Returns:
                    --------

                    - **`HttpResponse`**: Returning the address information
                    """,
            responses=GenerateAddressListXcodeAutoSchema.responses(),
            auto_schema=GenerateAddressListXcodeAutoSchema,
            tags=['Address Endpoints']
        )
    )
    @action(methods=['post'],
            detail=False,
            url_path='generate_address',
            permission_classes=[AllowAny, ])
    def generate_address(self, request):
        """
        Generating an addrress for the user
        :param request:
        :return: The generated results
        """

        serializer = AddressRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                """
                Create a processor object
                """
                block_chain_processor = BlockChain()
                """
                Request a new address to be generated
                """
                address = block_chain_processor.generate_address()
                """
                Check if the address is null
                """
                if address is not None:

                    user_id = request.data['user_id']
                    """
                    Add the address to the database for the user
                    """
                    record_to_be_stored= models.Address()

                    record_to_be_stored.address = address.address
                    record_to_be_stored.private = address.private
                    record_to_be_stored.public = address.public
                    record_to_be_stored.wif = address.wif
                    record_to_be_stored.user_id = User.objects.get(pk=user_id)
                    record_to_be_stored.save()

                    """
                    return the result
                    """
                    response_data = {
                        "address" : address.address,
                        "private" : address.private,
                        "public" : address.public,
                        "wif" : address.wif
                    }

                    return Response(response_data, content_type="application/json",
                                    status=status.HTTP_201_CREATED)

                else:
                    """
                    Raise an exception with related message
                    """
                    raise Exception("The address is not generated")
            except Exception as ex:
                """
                Return internal process error
                """
                response_data = {
                    "error": f"There is an internal process error. Error: {ex}",
                    "message": ""
                }
                return Response(response_data, content_type="application/json",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            """
            Rerun data validation error
            """
            response_data = {
                "error": "The data is not validated. Not able to proceed.",
                "message": ""
            }
            return Response(response_data, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(
        decorator=swagger_auto_schema(
            operation_summary="Get the list of addresses for a user",
            operation_description="""
                        Generate the list of addresses for the user

                        Parameters:
                        -----------

                        - **request** (`HttpRequest`): Here is the list of parameters:
                            - `user_id` : User ID requesting the address

                        Returns:
                        --------

                        - **`HttpResponse`**: Returning the address information
                        """,
            responses=GenerateAddressXcodeAutoSchema.responses(),
            auto_schema=GenerateAddressXcodeAutoSchema,
            tags=['Address Endpoints']
        )
    )
    @action(methods=['post'],
            detail=False,
            url_path='read_address_list',
            permission_classes=[AllowAny, ])
    def read_address_list(self, request):
        """
        Retrieve all address lists for a user.

        """

        serializer = AddressRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:

                """
                Retrieve the user information
                """

                user_id = request.data['user_id']
                address_list : QuerySet[models.Address] = models.Address.objects.filter(Q(user_id=user_id))

                response_data = [
                    {
                        "address": address.address,
                        "private": address.private[:4] + '*' * (len(address.private) - 30) ,
                        "public": address.public[:4] + '*' * (len(address.public) - 30),
                        "wif": address.wif[:4] + '*' * (len(address.wif) - 30)
                    }
                    for address in address_list]

                return Response(response_data, content_type="application/json",
                                status=status.HTTP_200_OK)

            except Exception as ex:
                """
                Return internal process error
                """
                response_data = {
                    "error": f"There is an internal process error. Error: {ex}",
                    "message": ""
                }
                return Response(response_data, content_type="application/json",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            """
            Rerun data validation error
            """
            response_data = {
                "error": "The data is not validated. Not able to proceed.",
                "message": ""
            }
            return Response(response_data, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(
        decorator=swagger_auto_schema(
            operation_summary="Return  the details of the address",
            operation_description="""
                           Return the details of the address

                           Parameters:
                           -----------

                           - **request** (`HttpRequest`): Here is the list of parameters:
                               - `address_id` : The target address ID

                           Returns:
                           --------

                           - **`HttpResponse`**: Returning the address details information
                           """,
            responses=GetAddressDetialsXcodeAutoSchema.responses(),
            auto_schema=GetAddressDetialsXcodeAutoSchema,
            tags=['Address Endpoints']
        )
    )
    @action(methods=['post'],
            detail=False,
            url_path='read_address_details',
            permission_classes=[AllowAny, ])
    def read_address_details(self, request):
        """
        Retrieve all address lists for a user.

        """

        serializer = AddressDetailRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:

                """
                Retrieve the user information
                """

                address_id = request.data['address_id']
                address_to_be_used = models.Address.objects.get(pk=address_id)
                address_details: QuerySet[models.Address] = models.AddressInfo.objects.filter(Q(address_id=address_id))

                if address_details.exists():

                    # Check if the time difference if it is more than 30 seconds
                    time_difference = (datetime.now() -
                                       datetime
                                            .fromisoformat(str(address_details.first().last_updated))
                                            .replace(tzinfo=None).replace(tzinfo=None))

                    if time_difference.total_seconds() > 30:

                        # update the database again
                        record_to_update = address_details.first()
                        block_chain_processor = BlockChain()
                        address_info = block_chain_processor.check_address_status(
                            wallet_address=address_to_be_used.address)

                        record_to_update.total_received = address_info.total_received
                        record_to_update.total_sent = address_info.total_sent
                        record_to_update.balance = address_info.balance
                        record_to_update.unconfirmed_balance = address_info.unconfirmed_balance
                        record_to_update.unconfirmed_n_tx = address_info.unconfirmed_n_tx
                        record_to_update.final_balance = address_info.final_balance
                        record_to_update.final_n_tx = address_info.final_n_tx
                        record_to_update.n_tx = address_info.n_tx
                        record_to_update.last_updated = datetime.now()

                        record_to_update.save()

                        response_data = {
                            "address": address_to_be_used.address,
                            "total_received": address_info.total_received,
                            "total_sent": address_info.total_sent,
                            "balance": address_info.balance,
                            "unconfirmed_balance": address_info.unconfirmed_balance,
                            "final_balance": address_info.final_balance,
                            "n_tx": address_info.n_tx,
                            "unconfirmed_n_tx": address_info.unconfirmed_n_tx,
                            "final_n_tx": address_info.final_n_tx,
                            "last_updated": datetime.now()
                        }

                    else:
                        # return the result
                        response_data = {
                            "address": address_to_be_used.address,
                            "total_received": address_details.first().total_received,
                            "total_sent": address_details.first().total_sent,
                            "balance": address_details.first().balance,
                            "unconfirmed_balance": address_details.first().unconfirmed_balance,
                            "final_balance": address_details.first().final_balance,
                            "n_tx": address_details.first().n_tx,
                            "unconfirmed_n_tx": address_details.first().unconfirmed_n_tx,
                            "final_n_tx": address_details.first().final_n_tx,
                            "last_updated": address_details.first().last_updated
                        }

                    return Response(response_data, content_type="application/json",
                                    status=status.HTTP_200_OK)
                else:
                    # Check for the online available information
                    block_chain_processor = BlockChain()
                    address_info = block_chain_processor.check_address_status(
                        wallet_address=address_to_be_used.address)



                    if(address_info is not None):
                        # Add the data to the database and return it as result
                        address_info_to_be_stored = models.AddressInfo()
                        address_info_to_be_stored.address_id = address_to_be_used
                        address_info_to_be_stored.total_received = address_info.total_received
                        address_info_to_be_stored.total_sent = address_info.total_sent
                        address_info_to_be_stored.balance = address_info.balance
                        address_info_to_be_stored.unconfirmed_balance = address_info.unconfirmed_balance
                        address_info_to_be_stored.unconfirmed_n_tx = address_info.unconfirmed_n_tx
                        address_info_to_be_stored.final_balance = address_info.final_balance
                        address_info_to_be_stored.final_n_tx = address_info.final_n_tx
                        address_info_to_be_stored.n_tx = address_info.n_tx
                        address_info_to_be_stored.last_updated = datetime.now()

                        address_info_to_be_stored.save()

                        response_data = {
                            "address": address_to_be_used.address,
                            "total_received": address_info.total_received,
                            "total_sent": address_info.total_sent,
                            "balance": address_info.balance,
                            "unconfirmed_balance": address_info.unconfirmed_balance,
                            "final_balance": address_info.final_balance,
                            "n_tx": address_info.n_tx,
                            "unconfirmed_n_tx": address_info.unconfirmed_n_tx,
                            "final_n_tx": address_info.final_n_tx,
                            "last_updated": datetime.now()
                        }

                        return Response(response_data, content_type="application/json",
                                        status=status.HTTP_200_OK)

                    else:
                        # Raise the error that no data found
                        raise FileNotFoundError("The information is not available!")

            except Exception as ex:
                """
                Return internal process error
                """
                response_data = {
                    "error": f"There is an internal process error. Error: {ex}",
                    "message": ""
                }
                return Response(response_data, content_type="application/json",
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            """
            Rerun data validation error
            """
            response_data = {
                "error": "The data is not validated. Not able to proceed.",
                "message": ""
            }
            return Response(response_data, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)

