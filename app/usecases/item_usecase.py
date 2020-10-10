from sqlalchemy.orm import Session

from app.repositories import item_repository
from app.schemas import item_schema
import redis
import json
from app.utils.db_utils import AlchemyEncoder

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return item_repository.get_items(db, skip=skip, limit=limit)

def get_item(db: Session, item_id: int):
    r = redis.Redis()
    redis_val = r.hgetall(f"item:{item_id}")
    print(len(redis_val))
    if (redis_val is None or len(redis_val) < 1):
        print('fetching data from database')
        item = item_repository.get_item(db, item_id=item_id)
        
        itemdetail = {f"data":json.dumps(item, cls=AlchemyEncoder)}
        r.hmset(f"item:{item.id}", itemdetail)
        return item
    else:
        print('fetching data from redis')
        item = json.loads(r.hget(f"item:{item_id}", "data"))
        return item

def create_user_item(db: Session, item: item_schema.ItemCreate, user_id: int):
    return item_repository.create_user_item(db=db, item=item, user_id=user_id)