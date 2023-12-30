from utils.swagger import XcodeAutoSchema
from serializers.user_endpoint_serialzers import AddUserSerializer, LoggedInUserSerializer
from serializers.address_endpoint_serializers import AddressResultSerializer
from rest_framework import serializers

# Begin Users Schemas
class AddUserXcodeAutoSchema(XcodeAutoSchema):
    python_template = "swagger/users/add_none_admin_user/python_sample.html"
    @classmethod
    def responses(cls):
        return {
            201: "User Created",
            409: "User already",
            400: "Bad Request"
        }

class LoginUserXcodeAutoSchema(XcodeAutoSchema):
    python_template = "swagger/users/login_user/python_sample.html"

    @classmethod
    def responses(cls):
        return {
            200: LoggedInUserSerializer(),
            401: "Invalid username or password",
            400: "Invalid request data"
        }

# End User's Schemas


# Begin Address Schemas
class GenerateAddressXcodeAutoSchema(XcodeAutoSchema):
    python_template = "swagger/users/add_none_admin_user/python_sample.html"
    @classmethod
    def responses(cls):
        return {
            201: AddressResultSerializer(),
            500: "Internal Server Error",
            400: "Bad Request"
        }

class GenerateAddressListXcodeAutoSchema(XcodeAutoSchema):
    python_template = "swagger/users/add_none_admin_user/python_sample.html"
    @classmethod
    def responses(cls):
        return {
            200: serializers.ListSerializer(child=AddressResultSerializer()),
            500: "Internal Server Error",
            400: "Bad Request"
        }
# End Address Schemas