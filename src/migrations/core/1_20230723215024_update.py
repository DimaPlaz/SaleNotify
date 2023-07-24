from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "client" RENAME TO "clients";
        ALTER TABLE "clients" RENAME COLUMN "name" TO "user";
        CREATE TABLE IF NOT EXISTS "games" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL UNIQUE,
    "discount" SMALLINT NOT NULL  DEFAULT 0,
    "image_link" VARCHAR(256) NOT NULL UNIQUE,
    "store_link" VARCHAR(256) NOT NULL UNIQUE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "clients" RENAME TO "client";
        ALTER TABLE "clients" RENAME COLUMN "user" TO "name";
        DROP TABLE IF EXISTS "games";"""
