from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "subscriptions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "client_id" INT NOT NULL REFERENCES "clients" ("id") ON DELETE CASCADE,
    "game_id" INT NOT NULL REFERENCES "games" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "subscriptions";"""
