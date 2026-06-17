from abc import ABC, abstractmethod

from redis import Redis


class RedisRepositoryInterface(ABC):
    @abstractmethod
    def __init__(self, redis_conn: Redis): pass

    @abstractmethod
    def insert(self, key: str, value: any): pass

    @abstractmethod
    def get_key(self, key: str): pass

    @abstractmethod
    def insert_hash(self, key: str, field: str,value: any): pass

    @abstractmethod
    def get_hash(self, key: str, field: str) -> any: pass

    @abstractmethod
    def insert_ex(self, key: str, value: any, ex: int): pass

    @abstractmethod
    def insert_hash_ex(self, key: str, field: str, value: any, ex: int): pass
