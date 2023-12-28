from pyrogram.types import InlineKeyboardButton

class Data:
    generate_single_button = [
        InlineKeyboardButton(" Generating Session ", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" Back ", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "Update Channel", url="https://t.me/realenzy"
            )
        ],
        [
            InlineKeyboardButton(" How to Use ", callback_data="help"),
            InlineKeyboardButton(" About ", callback_data="about"),
        ],
    ]  # Removed the "Other Bots" button

    START = """
    Hey there {}
    Welcome to {} 
    If you don't trust this bot,
    1) Stop reading this message
    2) Delete this chat
    Still reading?
    You can use me to generate pyrogram and telethon string session. Use below buttons to learn more!
    """

    HELP = """
    Commands

    /about - About the bot
    /help - This message
    /start - Start the bot
    /generate - Start generating session
    /cancel - Cancel the process
    /restart - Cancel the process
    """

    # About Message
    ABOUT = """
    **About This Bot**

    A Telegram bot to generate pyrogram and telethon string session from my master @titimothy
    """

    # Repo Message
    REPO = """
    What are you doing man?
    """
