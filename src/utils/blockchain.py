from app import settings
from .network import send_get_request, send_post_request
from .convertors import AddressConvertor


class BlockChain(object):
    """
    Class keeping all the functions related to the BlockChain Processes
    """

    def __init__(self):

        self.__address_end_point = \
            f"{settings.BlockCypher_BASE_ADDRESS}{settings.BlockCypher_COIN}/{settings.BlockCypher_CHAIN}/{settings.BlockCypher_Wallet_Address}"
        """
        internal variable to work the wallet
        """
        self.__transaction_end_point = \
            f"{settings.BlockCypher_BASE_ADDRESS}{settings.BlockCypher_COIN}/{settings.BlockCypher_CHAIN}/{settings.BlockCypher_Transaction_Address}"
        """
        internal variable to work on transactions
        """


    def generate_wallet(self):
        """
        generate a new address and return the following information:
            - The Address.
            - The public key.
            - The secret key.

        :return: Return this tuple (Address,Public Key,Secret Key)
        :rtype: (str,str,str)
        """

        address_to_user = f"{self.__address_end_point}?bech32=true"

        # Send the request to generate
        data = send_post_request(address_to_user)

        if data is not None:
            ## There is some data to look at

            address = AddressConvertor().from_json(value=data)

            if address is not None:
                print(address.address)
            else:
                print("No class available")


    def check_wallet_status(self):
        raise NotImplemented("This method has not been yet.")