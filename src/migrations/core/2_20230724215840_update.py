from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "games" ALTER COLUMN "name" TYPE VARCHAR(256) USING "name"::VARCHAR(256);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "games" ALTER COLUMN "name" TYPE VARCHAR(64) USING "name"::VARCHAR(64);"""
