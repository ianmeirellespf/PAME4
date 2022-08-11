from app.user.model import User
from app.user.schemas import Userschema
from app.utils.services import BaseCRUDServices

class UserServices(BaseCRUDServices[User, Userschema]):

    def get_by_email(self, email: str) -> User:
        return self.model.query.filter_by(email=email).first()


user_services = UserServices(User)