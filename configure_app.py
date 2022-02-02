from app.run_migration import run_migrations
from app.models.user import User
from app.config.settings import settings
from app.config.security import get_password_hash
import asyncio


async def initial_app_config():
    print("Run migrations")
    run_migrations(settings.DATABASE_URL)
    if not await User.objects.filter(email='admin@mail.com').exists():
        print("Create admin user")
        admin_properties = {
            "name": "admin",
            "email": "admin@mail.com",
            "hash_password": get_password_hash(settings.ADMIN_PASSWORD),
            "is_superuser": True
        }
        admin = User(**admin_properties)
        await admin.save()
    

if __name__ ==  "__main__":
    """
    Run the migrations and create the first user with superuser powers
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(initial_app_config())
    loop.close()