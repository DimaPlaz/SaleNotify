import emoji

start_message = emoji.emojize(
    "Hello, this bot exists to save money"
    ":hand_with_index_finger_and_thumb_crossed: "
    "on buying games on steam. "
    "You can find the game and subscribe to it. "
    "When the discount for this game changes, "
    "the bot will write to you."
)
subscribed_message = emoji.emojize("You has been subscribed :thumbs_up:")
unsubscribed_message = emoji.emojize("You has been unsubscribed :thumbs_up:")
start_search_msg = emoji.emojize("Enter the name of the game :backhand_index_pointing_down:")
nothing_was_found = emoji.emojize("Nothing was found for your request :disappointed_face:")
no_subscriptions = emoji.emojize("You don't have any subscriptions :disappointed_face:")
delete_all_subs = emoji.emojize("Are you sure you want to delete all your subscriptions :disappointed_face:")
deleted_subs = emoji.emojize("Subscriptions successfully deleted :like:")
canceled_deleting_subs = emoji.emojize("Subscriptions deletion canceled :like:")
unregistered_user = "First you need to click on the /start command"
share_steam_profile_msg = emoji.emojize("Please send me a link to your Steam profile:backhand_index_pointing_down:\n"
                                        "To do this, you can share the profile from the Steam application "
                                        "or paste the link directly from the browser if you are using a PC.")
wishlist_sync_starter_msg = emoji.emojize(":thumbs_up: Synchronization with the Steam wishlist has started, "
                                          "expect good news.")

search_button = emoji.emojize(":magnifying_glass_tilted_left:search")
yammy_button = emoji.emojize(":fire:Yummy:fire:")
subs_button = emoji.emojize(":bell:subs")
delete_subs_button = emoji.emojize(":bell_with_slash:delete subs")
steam_wishlist_button = emoji.emojize(":eyes::open_book::video_game:import steam wishlist")
