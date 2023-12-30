from .views import UserManagement


routes = [
    {'regex': r'rest', 'viewset': UserManagement, 'basename': 'Rest'}
]