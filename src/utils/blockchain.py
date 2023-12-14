from app import settings


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

        raise NotImplemented("This method has not been yet.")

    def check_wallet_status(self):