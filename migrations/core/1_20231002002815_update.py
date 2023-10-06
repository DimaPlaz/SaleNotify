from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "games" ADD "search_field" VARCHAR(512) NOT NULL  DEFAULT '';
        ALTER TABLE "games" ADD "review_count" INT NOT NULL  DEFAULT 0;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "games" DROP COLUMN "search_field";
        ALTER TABLE "games" DROP COLUMN "review_count";"""
