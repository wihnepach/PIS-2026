from infrastructure.config.database import Base, engine
from infrastructure.adapter.outgoing.request_repository import SessionOrm

Base.metadata.create_all(bind=engine)
print("Tables created successfully")