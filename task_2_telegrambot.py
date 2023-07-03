import telebot
import requests
bot = telebot.TeleBot('6214479372:AAFPfyTSkrQ-Q2JFaTyO7bSD6_7KIr6YU3g')
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, do you want to search for some Gifs? Please enter some key words.")
@bot.message_handler(func=lambda msg: True)
def my_answer(message):
    def give_gif(query):
        images = 1
        url = "https://api.giphy.com/v1/gifs/search"
        querystring = {"api_key":"l1JwJxvrqNVyHxmNHE61xgmHz1V4IpSx","q":query.text,"limit":images,"offset":"0"}
        my_response = requests.request("GET", url, params=querystring)
        return  my_response
    my_response = give_gif(message)
    my_response = my_response.json()['data'][0]['url']
    bot.reply_to(message, my_response)
bot.infinity_polling()