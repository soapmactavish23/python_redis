from src.data.product_finder import ProductFinder
from src.main.server.server_setting import redis_connection_handle, sqlite_connection_handle
from src.models.redis.repository.redis_repository import RedisRepository
from src.models.sqlite.repository.products_repository import ProductRepository


def product_finder_composer():
    redis_conn = redis_connection_handle.get_connection()
    sqlite_conn = sqlite_connection_handle.get_connection()

    redis_repo = RedisRepository(redis_conn)
    product_repo = ProductRepository(sqlite_conn)

    return ProductFinder(redis_repo, product_repo)