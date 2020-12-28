from telethon import TelegramClient, sync, events
import winsound
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
api_id = 2783469
api_hash = 'fd577f8634d249fee192cdb9aabddc04'

client = TelegramClient('session_name', api_id, api_hash)
@client.on(events.NewMessage(incoming=True))
async def normal_handler(event):
	print(event)
	msg = event.message.to_dict()['message']
	group_link = 'https://t.me/joinchat/EQntnhjjVPqX3ipi1vT6jA'
	await client.connect()
	entity = await client.get_entity(group_link)
	# print(entity)
	await client.send_message(entity=entity,message=f'сообщение {msg}')
	msg  = msg.split()
	necwords = [
	'сайт',
	'разработчик',
	'бот',
	'верстка',
	'верстолог', 
	'ботов', 
	'сайтолог', 
	'wordpress', 
	'django',
	'telegram',
	'магазин',
	'сайт']
	badwords = [
	'я',
	'помогу',
	]
	isArleadySignaled = False
	firstStep = False
	# print(' '.join(msg))
	# print(event.message.to_dict()['message'])

	for i in necwords:
		keyword = i
		for m in msg:
			if fuzz.ratio(keyword, m) > 80:
				print(f' good {fuzz.ratio(keyword, m)}')
				firstStep = True
	secondStep = False
	for i in badwords:
		keyword = i
		for m in msg:
			if fuzz.ratio(keyword, m) > 80:
				print ('bad ' + str(fuzz.ratio(keyword, m)))
				secondStep = False
	if firstStep and secondStep:
		print(' '.join(msg))
		isArleadySignaled = True
		winsound.PlaySound('SystemAsterisk', 1)

	# print(msg)
client.start()
# group_link = 'https://t.me/joinchat/EQntnhjjVPqX3ipi1vT6jA'
# entity = client.get_entity(group_link)
# # client.send_message(entity=entity, message="Сообщение из бота")
# def send(masg):
# 	client.send_message(entity=entity, message=masg)
# 	print('Сообщение отправлено в чат')
client.run_until_disconnected()
