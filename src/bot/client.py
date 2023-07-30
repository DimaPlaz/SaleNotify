class APIClient:
    def __init__(self, base_url):
        self._base_url = base_url

    async def search_games(self, pattern: str):
        ...
