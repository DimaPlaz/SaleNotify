from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "games" ALTER COLUMN "store_link" TYPE VARCHAR(512) USING "store_link"::VARCHAR(512);
        ALTER TABLE "games" ALTER COLUMN "image_link" TYPE VARCHAR(512) USING "image_link"::VARCHAR(512);
        ALTER TABLE "games" ALTER COLUMN "name" TYPE VARCHAR(512) USING "name"::VARCHAR(512);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "games" ALTER COLUMN "store_link" TYPE VARCHAR(256) USING "store_link"::VARCHAR(256);
        ALTER TABLE "games" ALTER COLUMN "image_link" TYPE VARCHAR(256) USING "image_link"::VARCHAR(256);
        ALTER TABLE "games" ALTER COLUMN "name" TYPE VARCHAR(256) USING "name"::VARCHAR(256);"""
