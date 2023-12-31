from .views import UserManagement, AddressManagement, TransactionsManagement


user_routes = [
    {'regex': r'rest', 'viewset': UserManagement, 'basename': 'Rest'}
]

address_routes = [
    {'regex': r'rest', 'viewset': AddressManagement, 'basename': 'Rest'}
]

transaction_routes = [
    {'regex': r'rest', 'viewset': TransactionsManagement, 'basename': 'Rest'}
]