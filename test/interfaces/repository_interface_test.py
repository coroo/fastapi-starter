from app.interfaces.api_interfaces import RepositoryInterface
from app.repositories.item_repository import ItemRepository
from app.repositories.user_repository import UserRepository

ItemRepository()
UserRepository()


def test_item_repository():
    assert issubclass(ItemRepository, RepositoryInterface)


def test_user_repository():
    assert issubclass(UserRepository, RepositoryInterface)
