from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "clients" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "user" VARCHAR(64),
    "chat_id" BIGINT NOT NULL
);
CREATE TABLE IF NOT EXISTS "games" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(512) NOT NULL UNIQUE,
    "discount" SMALLINT NOT NULL  DEFAULT 0,
    "image_link" VARCHAR(512) NOT NULL,
    "store_link" VARCHAR(512) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "subscriptions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "client_id" INT NOT NULL REFERENCES "clients" ("id") ON DELETE CASCADE,
    "game_id" INT NOT NULL REFERENCES "games" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
