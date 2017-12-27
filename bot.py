import teletwit_bot.common as common
from telegram.ext import Updater
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import  ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import datetime


# from telegram import Updater

# command handlers
# rough draft of coin list(buttons) that users will be able to choose from
# updates*** create dynamic button creation or even better checklist

def subscribe(bot, update):
    last_name = update.message.from_user.last_name
    if update.message.chat_id not in common.subscribers.keys():
        common.subscribers[update.message.chat_id] = { "chat_id": update.message.chat_id,
                                                       "first_name": update.message.from_user.first_name,
                                                       "user_name": last_name,
                                                       "coins" :[]
                                                     }
        print(common.subscribers[update.message.chat_id].keys())
        print(common.subscribers)
        user = update.message.chat.id
        print(user)

        common.saveSubscribers(common.subscribers)

        #common.subscribers["first_name"].append(update.message.from_user.first_name)
        #common.subscribers["last_name"].append(update.message.from_user.last_name)
        #common.subscribers["username"].append(str(update.message.from_user.username))
        #common.subscribers["user_id"].append(update.message.from_user.id)
        print(str(update.message.from_user.first_name))
        print(str(update.message.from_user.id))

        bot.sendMessage(update.message.chat_id, text='Subscribed!')
        common.saveSubscribers(common.subscribers)

    else:
        bot.sendMessage(update.message.chat_id, text='Already Subscribed!')


def unsubscribe(bot, update):
    if update.message.chat_id in common.subscribers["chat_id"]:
        common.subscribers["chat_id"].remove(update.message.chat_id)
        #common.subscribers["sub_date"].remove(str(update.message.date))
        common.subscribers["first_name"].remove(update.message.from_user.first_name)
        common.subscribers["last_name"].remove(update.message.from_user.last_name)
        #common.subscribers["username"].remove(update.message.from_user.username)
        #common.subscribers["user_id"].remove(update.message.from_user.id)
        bot.sendMessage(update.message.chat_id, text='Unsubscribed!')
        common.saveSubscribers(common.subscribers)
    else:
        bot.sendMessage(update.message.chat_id, text='You need to subscribe first!')


def hustlers(bot, update, answer, query):
    print("hello")
    chat_id = query.message.chat_id
    print(chat_id)
    bot.sendMessage(chat_id, text='hello!')

    if answer not in common.subscribers[chat_id].keys():

            print("did it pass")
            common.subscribers[chat_id][answer] = 1
            print("gettint there")
            common.saveSubscribers(common.subscribers)
            common.subscribers[user][answer] = 5
            print("gettint therew")
            common.subscribers ["coins"] = 5
            common.saveSubscribers(common.subscribers)
            #common.subscribers["coins"].append(answer)

            common.saveSubscribers(common.subscribers)



def follow(bot, update):

    last_name = update.message.from_user.last_name
    if update.message.chat_id not in common.subscribers.keys():
        common.subscribers[update.message.chat_id] = {"chat_id": update.message.chat_id,
                                                      "first_name": update.message.from_user.first_name,
                                                      "user_name": last_name,
                                                      "coins": []
                                                      }
        print(common.subscribers[update.message.chat_id].keys())
        print(common.subscribers)
        user = update.message.chat.id
        print(user)



    keyboard = [[InlineKeyboardButton("Walton (WTC)", callback_data='Walton'),
                 InlineKeyboardButton("Ether (ETH)", callback_data='Ether')],

                [InlineKeyboardButton("Bitcoin (BTC)", callback_data='Bitcoin'),
                 InlineKeyboardButton("Centra (CTR)", callback_data='Centra')],

                [InlineKeyboardButton("Ethos (BQX)", callback_data='Ethos'),
                 InlineKeyboardButton("MIOTA (IOTA)", callback_data='MIOTA')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('You are now subscribed')
    update.message.reply_text('Please Select the coins you would like to be updated on :', reply_markup=reply_markup)



def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="You are now following: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

    answer = "{}".format(query.data)
    answers = { "Walton" : "903434091650883586", "Ether":2312333412, "Bitcoin":357312062, "Centra":884936655437791232,
              "Ethos":"862007728956485632", "MIOTA":3992601857}

    print("cat")

    hustlers(bot,update,answer, query)


def bot_main(bot_token=""):
    # Create the EventHandler and pass it your bot's token.
   # updater = Updater(token=bot_token)
    updater = Updater(token="474430462:AAEfUyEsazaBoGE30jcYBa03kPFnShrFQ68")


    common.bot = updater.bot
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('follow', follow))
    dp.add_handler(CommandHandler("subscribe", subscribe))
    dp.add_handler(CommandHandler("unsubscribe", unsubscribe))
   # dp.add_handler(CommandHandler("hustlers", hustlers))
    dp.add_handler(CallbackQueryHandler(button))


    # Start the Bot
    updater.start_polling(timeout=5)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()
