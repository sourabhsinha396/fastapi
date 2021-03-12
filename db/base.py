# Import all the models, so that Base has them before being
# imported by Alembic
# In other words they can be used by target_metadata in alembic/env.py

from db.base_class import Base
from db.models.demo import Item
from db.models.cleanings import Cleanings
from db.models.users import  Users