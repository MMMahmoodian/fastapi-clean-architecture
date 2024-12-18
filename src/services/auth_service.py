"""It's usually a good idea to separate your controller and business logic. This can be done with adding service layers"""
class AuthService:
    @staticmethod
    def is_user_authorized(user, password):
        return user == "admin" and password == "123456"