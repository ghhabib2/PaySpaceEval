from abc import ABC, abstractmethod
from serializers import blockchain_serializers
from serializers.blockchain_serializers import Wallet, Transaction, Address
import json

class Convertor(ABC):
    """
    Converting the target objects to json and back to the object
    """

    @abstractmethod
    def to_json(self):
        """
        Convert to Json

        return: Json string
        """
        pass

    @abstractmethod
    def from_json(self, value:str):
        """
        Get the Json response and convert it back to the object.
        :param value: Value that needed to be converted to the object
        :return: Return the object
        """
        pass


class WalletConvertor(Convertor):
    """
    Converting the Wallet data to the jason format and back to the object
    """
    def __init__(self, target_object:Wallet = None):
        """

        :param target_object: Target objcet that neede to be converted to the Json data
        """
        self.__target_object = target_object
        """
        Internal variable to handle the object
        """

    def to_json(self):
        return Wallet(self.__target_object).data;

    def from_json(self, value:str):
        self.__target_object = Wallet(data=json.loads(value.decode('utf-8')))
        temp_wallet = Wallet()

        # if self.__target_object.is_valid():
        if self.__target_object.is_valid():
            for key, value in self.__target_object.validated_data.items():
                setattr(temp_wallet, key, value)
            return temp_wallet
        else:
            return None

class TransactionConvertor(Convertor):
    """
    Converting the Wallet data to the jason format and back to the object
    """
    def __init__(self, target_object:Transaction = None):
        """

        :param target_object: Target objcet that neede to be converted to the Json data
        """
        self.__target_object = target_object
        """
        Internal variable to handle the object
        """

    def to_json(self):
        return Transaction(self.__target_object).data

    def from_json(self, value:str):
        self.__target_object = Transaction(data=value)
        if self.__target_object.is_valid():
            return self.__target_object
        else:
            return None


class AddressConvertor(Convertor):
    """
    Converting the Wallet data to the jason format and back to the object
    """
    def __init__(self, target_object:Address = None):
        """

        :param target_object: Target objcet that neede to be converted to the Json data
        """
        self.__target_object = target_object
        """
        Internal variable to handle the object
        """

    def to_json(self):
        return Transaction(self.__target_object).data

    def from_json(self, value:str):

        self.__target_object = Address(data=json.loads(value.decode('utf-8')))
        temp_address = Address()

        # if self.__target_object.is_valid():
        if self.__target_object.is_valid():
            for key, value in self.__target_object.validated_data.items():
                setattr(temp_address, key, value)
            return temp_address
        else:
            return None

def __create_object_from_serializer_data(serializer_class, validated_data):
    obj = serializer_class(data=validated_data)
    if obj.is_valid():
        return obj.save()  # Save the object instance if valid
    else:
        raise ValueError("Invalid data for serializer")