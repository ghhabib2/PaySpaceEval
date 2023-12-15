from utils import blockchain
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

blockchain_manager = blockchain.BlockChain()

blockchain_manager.generate_wallet()