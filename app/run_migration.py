import os
from alembic.config import Config
from alembic import command

from app.config.settings import settings

def run_migrations(db_uri: str = None) -> None:
    dirname = os.path.dirname(__file__)
    script_location = os.path.join(dirname, '../database/alembic')
    config_location = os.path.join(dirname, '../database/alemcic.ini')
    alembic_cfg = Config(config_location)
    alembic_cfg.set_main_option('script_location', script_location)
    
    db_uri = os.getenv('DATABASE_URL', db_uri)

    if db_uri:
        alembic_cfg.set_main_option('sqlalchemy.url', db_uri)

    command.upgrade(alembic_cfg, 'head')

def run_migrations_test(db_uri: str = None) -> None:
    dirname = os.path.dirname(__file__)
    script_location = os.path.join(dirname, '../database/alembic')
    config_location = os.path.join(dirname, '../database/alemcic.ini')
    alembic_cfg = Config(config_location)
    alembic_cfg.set_main_option('script_location', script_location)
    
    db_uri = os.getenv('DATABASE_URL', db_uri)

    if db_uri:
        alembic_cfg.set_main_option('sqlalchemy.url', db_uri)

    command.downgrade(alembic_cfg, 'base')
    command.upgrade(alembic_cfg, 'head')

if __name__ ==  "__main__":
    run_migrations(settings.DATABASE_URI)