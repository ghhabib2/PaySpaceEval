from .views import UserManagement, AddressManagement


user_routes = [
    {'regex': r'rest', 'viewset': UserManagement, 'basename': 'Rest'}
]

address_routes = [
    {'regex': r'rest', 'viewset': AddressManagement, 'basename': 'Rest'}
]