from src.models.redis.repository.interfaces.redis_repository_interface import RedisRepositoryInterface
from src.models.sqlite.repository.products_repository_interface import ProductRepositoryInterface


class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductRepositoryInterface) -> None:
        self.__redis_repo = redis_repo
        self.__sqlite_repo = products_repo