class SteamBadProfileUrlError(Exception):
    def __init__(self, message="Incorrect link to steam profile"):
        self.message = message
        super().__init__(self.message)


class SteamEmptyWishlistError(Exception):
    def __init__(self, message="Your wishlist is empty"):
        self.message = message
        super().__init__(self.message)


class SteamWishlistWithoutPaidGamesError(Exception):
    def __init__(self, message="There are no paid games in your wishlist"):
        self.message = message
        super().__init__(self.message)
