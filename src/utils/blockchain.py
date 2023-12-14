from app import settings


class BlockChain(object):
    """
    Class keeping all the functions related to the BlockChain Processes
    """

    def __init__(self):

        self.__address_end_point = \
            f"{settings.BlockCypher_BASE_ADDRESS}{settings.BlockCypher_COIN}/{settings.BlockCypher_CHAIN}/{settings.BlockCypher_Wallet_Address}"
        """
        internal variable generating the wallet address
        """
        self.__transaction_end_point = \
            f"{settings.BlockCypher_BASE_ADDRESS}{settings.BlockCypher_COIN}/{settings.BlockCypher_CHAIN}/{settings.BlockCypher_Transaction_Address}"

    def generate_wallet(self):
        """
        This will generate a wallet

        :return:
        """