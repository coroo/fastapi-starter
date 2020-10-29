from app.interfaces.api_interfaces import ServiceInterface
from app.usecases.item_service import ItemService
from app.usecases.user_service import UserService

ItemService()
UserService()


def test_item_repository():
    assert issubclass(ItemService, ServiceInterface)


def test_user_repository():
    assert issubclass(UserService, ServiceInterface)
