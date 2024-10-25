ASSETS_DIR = 'assets/'
TEXTS_DIR = f'{ASSETS_DIR}texts/'

# SILENT
####################################################################################################
#TRAVELER
TRAVELER_SPEECH_PATH = f'{TEXTS_DIR}traveller_speech.txt'

#UNDEAD
UNDEAD_SPEECH_PATH = f'{TEXTS_DIR}undead_speech.txt'
####################################################################################################


# SPIRITS
####################################################################################################
#MAVKA
MAVKA_SPEECH_PATH = f'{TEXTS_DIR}mavka_speech.txt'
MAVKA_RIDDLE_PATH = f'{TEXTS_DIR}mavka_riddle.txt'

#DEMON
DEMON_SPEECH_PATH = f'{TEXTS_DIR}demon_speech.txt'
DEMON_RIDDLE_PATH = f'{TEXTS_DIR}demon_riddle.txt'

GIVE_TO_DEMON ='yes'
NOT_GIVE_TO_DEMON ='no'

DEMON_BRIBE = f"You have Varenucha in your inventory! Give it to the devil? ({GIVE_TO_DEMON}, {NOT_GIVE_TO_DEMON})"
DEMON_STEALS_COINS= "\nNot wise enough, as now I see!\
    \nThy coins now belong to me!\
    \nGood luck next time you, foolish brat!\
    \nFor thou hast lost, and that is that!"
DEMON_RETREATS = "\nImpressive, thou hast passed my test!\
    \nThy wits have saved thee from the worst!\
    \nEnjoy thy path, yet heed my call,\
    \nNext time it may not end so small!"
DEMON_GIVES_A_CHANCE = "\nThy life I seek, a tempting prize,\
    \nYet mercy lingers in my eyes.\
    \nIf thou bestow something of value,\
    \nThat trinket may, if I wish, save thou."
DEMON_KILLS = "\nAlas, thou nothing hast to keep,\
    \nAnd now thy fate is dark and steep.\
    \nFor he who comes with naught to share,\
    \nShall meet his end, lost to despair!" 
####################################################################################################


# HUMANS
####################################################################################################
#PEASENT
# Constants for trade options
TRADE_YES = 'yes'
TRADE_NO = 'no'
PEASANT_INTRO = "Good evening. I'm just a poor peasant, trying to survive in this wilderness."
PEASANT_TRADE_PROMPT = "Do you have anything to trade?"
PEASANT_MULTI_ITEM_PROMPT = f"You have several items. Do you want to trade one for a hint? ({TRADE_YES}/{TRADE_NO}): "
PEASANT_NO_TRADE = "Without a trade, I cannot help you. Perhaps you should head west."
PEASANT_NO_ITEMS = "You have nothing to trade! Maybe next time."
PEASANT_TRADE_THANKS = "Thank you for {}!"
PEASANT_REMAINING_SPIRITS = "There are {} spirits you have yet to meet."
PEASANT_REMAINING_PEOPLE = "There are {} people you have yet to meet."
PEASANT_NO_ITEMS_FOR_TRADE = "You don't have enough items to trade."
PEASANT_ACTION = "I am Peasant"
# Minimum items needed for hint trade
HINT_THRESHOLD = 1


# MAN
MAN_ACTION = "I am Man"


# MERCHANT
VISIT_SHOP_YES = MARCHANT_TRADE_YES = 'yes'
VISIT_SHOP_NO = MARCHANT_TRADE_NO = 'no'
# Number of coins for each item
VARENUCHA = 8
BARTKA = 10
WORMWOOD = 15
# Shop pointers
BUY_VARENUCHA = '1'
BUY_WORMWOOD = '2'
BUY_BARTKA = '3'
BUY_NOTHING = '4'
MERCHANT_INTRO = "Good night, fellow! Greetings, traveler! Welcome to my humble shop!"
SHOP_CHOICE = f"Do you seek for any treasures or supplies in these enchanted woods? ({VISIT_SHOP_YES}/{VISIT_SHOP_NO}) : "
VISIT_SHOP_NO = "Ah, I understand, traveler. Perhaps another time! The forest holds many mysteries - stay safe on your journey!"
DISPLAY = "Excellent choice, traveler! I have a fine selection of things for you. Take a look: \
\n - I have plenty of bottles of varenucha. Who knows what company you might encounter on your journey?\
\n - I have bundles of wormwood. Tie one to your belt, and it will shield you from any impure forces lurking in the shadows!\
\n - I have copper bartkas. Acquire one, and no highwayman will dare cross your path!"
# Buying goods
GOODS = f"\nWhat would you choose?\
\n1 - Varenucha (8 coins)\
\n2 - Wormwood (15 coins)\
\n3 - Bartka (10 coins)\
\n4 - Nothing\
\nEnter a number ({BUY_VARENUCHA}/{BUY_WORMWOOD}/{BUY_BARTKA}/{BUY_NOTHING}) : "
MERCHANT_PURCHASE_THANKS = "Ah, a wise choice, traveler! May it serve you well on your adventures. If you need anything else, don’t hesitate to return!"
MERCHANT_NO_PURCHASE = "Very well, traveler! Sometimes it's best to save your coins for a more pressing need. If you change your mind, my wares will always be here. Safe travels!"
MERCHANT_NO_COINS = "Ah, it seems your purse is light, traveler. No worries! Perhaps you have something to trade or can come back when your fortunes improve!"
MERCHANT_NOT_ENOUGH_COINS = "Alas, it seems you don't have enough coins for this purchase. But I still want to offer you some help!"
# Trading items
MERCHANT_TRADE = "Do you want to trade something?"
MERCHANT_TRADE_OPTION = f"You have some items. Do you want to trade them for something else? ({MARCHANT_TRADE_YES}/{MARCHANT_TRADE_NO}) : "
TRADES = "I will trade any of your items for whatever you want!"
MERCHANT_TRADE_THANKS = "Thank you for the trade! Hope {} serves you well!"
MERCHANT_TRADE_NOT_OCCURED = "No worries! If you change your mind, I will be here."


# BANDIT
PAY_YES = 'yes'
PAY_NO = 'no'
PAY_ITEMS = 'items'
PAY_COINS = 'coins'
BANDIT_INTRO = "Hey there, traveler! How about a little 'donation' to support my... endeavors?"
BANDIT_PAY_PROMPT = f"Pay me with 2 items or 10 coins or face the consequences! Do you pay? ({PAY_YES}/{PAY_NO}): "
BANDIT_PAY_WITH_PROMPT=f"What do youn want to pay me with? ({PAY_ITEMS}/{PAY_COINS}): "
BANDIT_KILL_MESSAGE = "You refused to pay! The Bandit attacks and kills you."
BANDIT_PAY_THANKS = "Wise choice. You may go, for now..."
ITEMS_PAY_AMOUNT = 2
COINS_PAY_AMOUNT = 10