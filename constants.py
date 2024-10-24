ASSETS_DIR = 'assets/'
TEXTS_DIR = f'{ASSETS_DIR}texts/'

#TRAVELER
TRAVELER_SPEECH_PATH = f'{TEXTS_DIR}traveller_speech.txt'


#UNDEAD
UNDEAD_SPEECH_PATH = f'{TEXTS_DIR}undead_speech.txt'


#MAVKA
MAVKA_SPEECH_PATH = f'{TEXTS_DIR}mavka_speech.txt'
MAVKA_RIDDLE_PATH = f'{TEXTS_DIR}mavka_riddle.txt'


#PEASENT
# Constants for trade options
TRADE_YES = 'yes'
TRADE_NO = 'no'
PEASANT_INTRO = "Good evening. I'm just a poor peasant, trying to survive in this wilderness."
PEASANT_TRADE_PROMPT = "Do you have anything to trade?"
PEASANT_MULTI_ITEM_PROMPT = f"You have several items. Do you want to trade one for a hint? ({TRADE_YES}/{TRADE_NO}): "
PEASANT_NO_TRADE = "Without a trade, I cannot help you. Perhaps you should head west."
PEASANT_NO_ITEMS = "You have nothing to trade! Maybe next time."
PEASANT_TRADE_THANKS = "Thank you for the {}!'"
PEASANT_REMAINING_SPIRITS = "There are {} spirits you have yet to meet."
PEASANT_REMAINING_PEOPLE = "There are {} people you have yet to meet."
PEASANT_NO_ITEMS_FOR_TRADE = "You don't have enough items to trade."
PEASANT_ACTION = "I am Peasant"
# Minimum items needed for hint trade
HINT_THRESHOLD = 1


# MAN
MAN_ACTION = "I am Man"


# MERCHANT
MERCHANT_ACTION = "I am Merchant"


# BANDIT
BANDIT_ACTION = "I am Bandit"
BANDIT_PAY_PROMPT = "Pay me with 2 items or face the consequences! Do you pay? (yes/no): "
BANDIT_KILL_MESSAGE = "You refused to pay! The Bandit attacks and kills you."
BANDIT_PAY_THANKS = "Wise choice. You may go, for now..."
PAY_AMOUNT = 2