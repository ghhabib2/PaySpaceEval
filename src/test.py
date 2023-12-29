import json

from utils import blockchain
from django.core.wsgi import get_wsgi_application
import os
import asyncio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

blockchain_manager = blockchain.BlockChain()

data = asyncio.run(blockchain_manager.send_transaction(
    input_address="tb1q7kwcglyj8gzvlt8xsmrg080fyrp55r9papjrye",
    output_address="tb1qp8plnpf0fd67f4ldkxjltcgs52us9tcm59eudv",
    value=10,
    public_keys=["02f5c60f6f5d5f1db0d6c72d732eec5f374fbe53ddd3d3ab2ac082469ba8279bb4"],
    private_kes=["a09c4d687c47e5f939e4d3748c8cf0aa217a528454d81d625a618f35b516d635"])
)





