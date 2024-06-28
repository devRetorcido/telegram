import  telebot
from telebot import types
#Anotaciones
# busar etiquetas top y super top
# buscar etiqueta de num wsap
# navegar hasta la pagina puntual

#TOKEN= '6837254324:AAHi9Mna4rrNAHhmDdwYiCTOGHQ80RbDOUg' este token es de poskksc
TOKEN= '7214033295:AAE3gAen4v9VkgpnNNwksQHivW7BdhTXJp8'


bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def send_welcome(message):
    bot.reply_to(message, 'Hola!, soy tu asistente de busqueda')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'solo respondo a start, hep y mostrar')

#@bot.message_handler(func=lambda m:True)
#def echo_all(message):
#    bot.reply_to(message,message.text)



@bot.message_handler(commands=['mostrar'])    
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1_nov=types.InlineKeyboardButton('Novedad',callback_data='mostrar_novedad')
    btn2_top=types.InlineKeyboardButton('Top',callback_data='mostar_top')
    btn3_stop=types.InlineKeyboardButton('Super Top',callback_data='mostar_supertop')
    markup.add(btn1_nov,btn2_top,btn3_stop)
    bot.send_message (message.chat.id,"Que quieres mirar?",reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'mostrar_novedad':
        bot.answer_callback_query(call.id, 'Estas nos las novedades')
    if call.data == 'mostar_top':
        bot.answer_callback_query(call.id, 'Chicas Top')
    if call.data == 'mostar_supertop':
        bot.answer_callback_query(call.id, 'chicas Super Top')        

@bot.message_handler(commands=['foto'])    
def send_imagen(message):
    img_url='https://images.ctfassets.net/23aumh6u8s0i/6uBzrqHNLlSAoER6HtgDN0/accd8f871b1de37f472b94da4346afa2/python-hero'
    bot.send_photo(chat_id=message.chat.id, photo=img_url, caption='mi imagen')




if __name__=="__main__":
    bot.polling(none_stop=True)
