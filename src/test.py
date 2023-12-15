from utils import blockchain
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

blockchain_manager = blockchain.BlockChain()

temp_wallet = blockchain_manager.check_wallet_status('tb1qvavgt9rwuc0jtylnmqpwrlpgdz8075n8503x7p')

if temp_wallet is not None:
    print(temp_wallet.txrefs.length)