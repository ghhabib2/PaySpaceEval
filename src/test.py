import json

from utils import blockchain
from django.core.wsgi import get_wsgi_application
import os
import asyncio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

blockchain_manager = blockchain.BlockChain()

data = asyncio.run(blockchain_manager.send_transaction(
    input_address="tb1q20d9ms9cz4nq6hgkcczp4lyjg8plh2cqfxkgg4",
    output_address="tb1qp8plnpf0fd67f4ldkxjltcgs52us9tcm59eudv",
    value=10,
    public_keys=["0209080758e248d0a78136970b3cc5d9b0d18098393be64becf109dde73501192a"],
    private_kes=["2c9543bcf7c6e74adee97c30832909ec09c86a2fc97df98dc8ac63b831381830"])
)





