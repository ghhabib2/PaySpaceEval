import json

from app import settings
from .network import send_get_request, send_post_request, send_secured_request, send_secured_async_request
from .convertors import AddressConvertor, WalletConvertor
from  serializers.blockchain_serializers import Address, Wallet
import blockcypher


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


    def generate_address(self):
        """
        generate a new address and return the following information:
            - The Address.
            - The public key.
            - The secret key.

        :return: Return this tuple (Address,Public Key,Secret Key)
        :rtype: Address
        """

        address_to_user = f"{self.__address_end_point}?bech32=true"

        # Send the request to generate
        data = send_post_request(address_to_user)

        if data is not None:
            ## There is some data to look at
            return AddressConvertor().from_json(value=data)
        else:
            return  None


    def check_address_status(self, wallet_address):
        """
        Retrieve all the wallet information and return it as a Wallet object

        :param str wallet_address : The address of the wallet we try to test

        :return: Return the wallet if it is existed and None if it is noe
        :rtype: Wallet
        """

        address_to_use = f"{self.__address_end_point}/{wallet_address}"

        data = send_get_request(address_to_use)

        if data is not None:
            return WalletConvertor().from_json(value=data)
        else:
            return None


    async def send_transaction(self, input_address, output_address, public_keys, private_kes,  value):
        """
            Send a new transaction based on the addresses
            :param str input_address : The address of the input wallet
            :param str output_address : The address of the output wallet
            :param float value: The Value of the transaction
            :param list public_keys: The public keys list for the wallets
            :param list private_kes: The private keys list for the wallets
            :return: Return the hash information to be processed later.
            :rtype: dict
            """

        def __generate_new_transaction(input_adr, output_adr, amount):
            """
            Generate an unsigned transaction based on the addresses
            """

            payload = {
                "fees" : 1,
                "inputs": [
                    {
                        "addresses": [input_adr]
                    }
                ],
                "outputs": [
                    {
                        "addresses": [output_adr],
                        "value": amount
                    }
                ]
            }
            """
            Payload to be sent to the endpoint
            """

            url = f"{self.__transaction_end_point}/new?token=0d1ac92ec45448089e2c0f42fece0276"

            result, code = send_secured_request(url=url,
                                        payload=json.dumps(payload))

            if code == 201:
                return result
            else:
                return None

        def __sign_transaction(tx_to_sign :dict, priv_key :list, pub_keys: list):
            """
            Signing the unsigned transaction

            :return: Return the signed hashed key to be broadcaster
            """

            return blockcypher.make_tx_signatures(txs_to_sign=tx_to_sign,
                                                  privkey_list=priv_key,
                                                  pubkey_list=pub_keys)

        unsigned_tx = __generate_new_transaction(input_address, output_address, value)
        """
        This value contains all the necessery information for the unsigned transaction information
        """


        tx_to_sign = unsigned_tx["tosign"]
        pub_key_witness = [str(unsigned_tx["tx"]["outputs"][0]["script"])]
        print(list(pub_key_witness))
        signed_tx = __sign_transaction(tx_to_sign=tx_to_sign,
                                       priv_key=list(private_kes),
                                       pub_keys= list(public_keys))
        """
        Generates the list of signatures to be send
        """

        final_payload = unsigned_tx

        final_payload["signatures"] = [signed_tx[0]+'01']
        final_payload["pubkeys"] = public_keys


        print(json.dumps(final_payload))

        print("\n")


        address_to_use = f"{self.__transaction_end_point}/send?token=0d1ac92ec45448089e2c0f42fece0276"

        data = await send_secured_async_request(url=address_to_use, payload=final_payload)
        """
        Sending the transaction to the endpoint and returning the results
        """

        return data
