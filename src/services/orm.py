from sqlalchemy import select

from src.database.models import User, UserMailRu, UserVk, UserYandex
from src.services.db import DatabaseSessionService


class ORMService(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def add_user(self, user) -> dict:
        async with self.session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user.id

    async def get_user_email(self, email: str, hash_password: str) -> dict:
        async with self.session() as session:
            user = await session.execute(
                select(User).where(
                    User.email == email and User.hash_password == hash_password
                )
            )
            try:
                return user.scalar()
            except Exception as _ex:
                print(_ex)

    async def get_user_phone_number(
        self, phone_number: str, hash_password: str
    ) -> dict:
        async with self.session() as session:
            user = await session.execute(
                select(User).where(
                    User.phone_number == phone_number
                    and User.hash_password == hash_password
                )
            )
        try:
            return user.scalar()
        except Exception as _ex:
            print(_ex)

    async def get_user_email_vk(self, email: str) -> dict:
        async with self.session() as session:
            user = await session.execute(select(UserVk).where(UserVk.email == email))
            try:
                return user.scalar()
            except Exception as _ex:
                print(_ex)

    async def get_user_email_mail_ru(self, email: str) -> dict:
        async with self.session() as session:
            user = await session.execute(
                select(UserMailRu).where(UserMailRu.email == email)
            )
            try:
                return user.scalar()
            except Exception as _ex:
                print(_ex)

    async def get_user_email_yandex(self, email: str) -> dict:
        async with self.session() as session:
            user = await session.execute(
                select(UserYandex).where(UserYandex.email == email)
            )
            try:
                return user.scalar()
            except Exception as _ex:
                print(_ex)


    async def get_data(self, user_id: int) -> dict:
        async with self.session() as session:
            user = await session.execute(
                select(User).where(User.id == user_id)
            )
            try:
                return user.scalar()
            except Exception as _ex:
                print(_ex)
