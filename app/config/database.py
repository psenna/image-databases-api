import databases
import sqlalchemy

from app.config.settings import settings

database = databases.Database(settings.DATABASE_URL, force_rollback=settings.TEST_DATABASE)
metadata = sqlalchemy.MetaData()