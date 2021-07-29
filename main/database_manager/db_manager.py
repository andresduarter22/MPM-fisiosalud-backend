"""
db|_manager
    """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Sequence
from config import *

class BbManager:
    def __init__(self):
        self.url = f'mysql://{DB_USER_NAME}:{DB_USER_PASSWORD}@{DB_HOST_NAME}:{DB_PORT}/{DB_DATABASE}'
        self.engine = create_engine(self.url, echo=True)
        Session = sessionmaker(bind=self.engine)
        session = Session()

#CREATE
# working_area = WorkingArea(area_name='Pilates', area_total_capacity='5', availability=True)
# session.add(working_area)
# session.commit()

#SELECT
# for instance in session.query(WorkingArea):
#     print(instance.area_id, instance.area_name, instance.area_total_capacity, instance.availability)
# Base.metadata.create_all(engine)