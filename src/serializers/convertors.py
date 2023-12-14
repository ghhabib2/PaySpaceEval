from abc import ABC, abstractmethod
from serializers import blockchain_serializers
from serializers.blockchain_serializers import Wallet, Transaction


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
        self.__target_object = Wallet(data=value)
        if self.__target_object.is_valid():
            return self.__target_object
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