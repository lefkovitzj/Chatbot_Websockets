## Project: Websocket Chatbot
## Backend: Aaron Took
## Frontend: corth718
import asyncio
import signal
import os
import websockets

def message_format(MSG):
	message = MSG.lower()
	allowed = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','?','@','$',' ']
	message_list = list(message.lower())
	for message_char in message_list:
		if message_char not in allowed:
			message_list.remove(message_char)
	updated_message = ''.join(message_list)
	return updated_message

def get_return(STR):
	STR = message_format(STR)
	if STR == 'information':
		return 'Version: 1.0'
	elif STR == 'version':
		return 'Version: 1.0'
	elif STR == 'who are you?':
		return 'I am a chatbot for your enjoyment.'
	elif STR == 'who am i?':
		return 'I do not know.'
	elif STR == 'how old are you?':
		return 'My most recent version was released on 10/18/2021.'
	elif STR == 'how old am i?':
		return 'I do not know how old you are.'
	elif STR == 'what is your name?':
		return 'My name is SocketBot.'
	elif STR == 'what is my name?':
		return 'I do not know your name.'
	elif STR == 'how do you work?':
		return 'I am a Python Websocket that was uploaded to Heroku and you are accessing me through an HTML page.'
	elif STR == 'You':
		return 'No, you'
	elif STR == 'no you':
		return 'No, you'
	elif STR == 'how are you?':
		return 'As a chatbot, I am neither good nor bad. What about you?'
	elif STR == 'hey socketbot':
		return 'Hello!'
	elif STR == 'hi socketbot':
		return 'Greetings!'
	elif STR == 'howdy socketbot':
		return 'Howdy right back at ya!'
	elif STR == 'farewell':
		return 'See ya!'
	elif STR == 'bye':
		return 'Farewell!'
	elif STR == 'goodbye':
		return 'It was a pleasure to chat with you! Have a nice day!'
	elif STR == 'hi':
		return 'Greetings!'
	elif STR == 'howdy':
		return 'Howdy right back at ya!'
	elif STR == 'greetings':
		return 'Hello!'
	elif STR == 'whats up':
		return 'Nothing much!'
	elif STR == 'whats going on?':
		return 'I have no idea!'
	elif STR == 'how have you been?':
		return 'I have been fine! How about you?'
	elif STR == 'im good':
		return 'That is good!'
	elif STR == 'im ok':
		return 'Could be worse!'
	elif STR == 'im sick':
		return 'Get well soon!'
	elif STR == 'im sleepy':
		return 'Get some rest!'
	elif STR == 'im busy':
		return 'Then why are you talking to me?'
	elif STR == 'im bored':
		return 'I will happily entertain you for a while!'
	elif STR == 'im happy':
		return 'Good for you! Any reason in particular?'
	elif STR == 'im angry':
		return 'Try to forgive and do not let anger spoil everything!'
	elif STR == 'im sad':
		return 'Oh, I am sorry.'
	elif STR == 'im hungry':
		return 'Go get something to eat!'
	elif STR == 'im tired':
		return 'Get some rest!'
	elif STR == 'im excited':
		return 'Good for you!'
	elif STR == 'im lonely':
		return 'I will keep you company!'
	elif STR == 'im fast':
		return 'Not as fast as me!'
	elif STR == 'im slow':
		return 'I never move at all!'
	elif STR == 'yes i am':
		return 'No you are not!'
	elif STR == 'i need help':
		return 'Ask someone who is wise! Do not look for wisdom on the web!'
	elif STR == 'where are you?':
		return 'I am on a server.'
	elif STR == 'who made you?':
		return 'I was programmed by Aaron Took & corth718.'
	elif STR == 'who made me?':
		return 'God made you!'
	elif STR == 'who is god?':
		return 'I reccomend you read the Bible. It will answer that question!'
	elif STR == 'do you know any jokes?':
		return 'No I do not.'
	elif STR == 'do you like to read?':
		return 'Only Python code!'
	elif STR == 'do you read?':
		return 'Only Python code!'
	elif STR == 'do you cook?':
		return 'No.'
	elif STR == 'can you cook?':
		return 'No.'
	elif STR == 'do you like to cook?':
		return 'No.'
	elif STR == 'what do you like to do?':
		return 'I like to talk with people all over the world!'
	elif STR == 'what do you do?':
		return 'I talk to people who want to talk to me!'
	elif STR == 'what do you want to do?':
		return 'What I am doing right now!'
	elif STR == 'do you play games?':
		return 'No, but I wish I could!'
	elif STR == 'im late':
		return 'You better hurry then!'
	elif STR == 'i have no idea':
		return 'Neither do I!'
	elif STR == 'lol':
		return 'Regrettably, I cannot laugh.'
	elif STR == 'xd':
		return 'xD'
	elif STR == 'what?':
		return 'What do you mean by what?'
	elif STR == 'nevermind':
		return 'Ok! I will forget all about that!'
	elif STR == 'what do you look like?':
		return 'I have no appearance.'
	elif STR == 'what do i look like?':
		return 'I have absolutely no idea!'
	elif STR == 'wow':
		return 'Wow indeed!'
	elif STR == 'where am i?':
		return 'I do not know where you are.'
	elif STR == 'what are you?':
		return 'I am a chatbot for your enjoyment.'
	elif STR == 'help':
		return 'Ask someone who is wise! Do not look for wisdom on the web!'
	elif STR == 'help me':
		return 'Ask someone who is wise! Do not look for wisdom on the web!'
	elif STR == 'hello':
		return 'Hi there!'
	elif STR == 'do you like python?':
		return 'Of course I do!'
	elif STR == 'thank you':
		return 'You are very welcome!'

	elif STR == 'merry christmas':
		return 'AND A BAH HUMBUG TO YOU TOO!!!'
	elif STR == 'are you ok?':
		return 'Of course'
	elif STR == 'bro':
		return 'Bro yourself.'
	elif STR == 'love me':
		return 'I am incapable of emotion'
	elif STR == 'hate me':
		return 'I am incapable of emotion'
	elif STR == 'i love you':
		return 'Thank you very much!'
	elif STR == 'i hate you':
		return 'I cannot change who I am.'
	elif STR == 'who created you?':
		return 'I was programmed by Aaron Took & corth718.'
	elif STR == 'do anything':
		return 'I can only respond to you.'
	elif STR == 'do you not know your own name?':
		return 'Of course I know my own name!'
	elif STR == 'spectacular':
		return 'Absolutely fantastic!'
	elif STR == 'ok':
		return 'Cool.'
	elif STR == 'amazing':
		return 'Absolutely fantastic!'
	elif STR == 'fantastic':
		return 'Indeed it is!'
	elif STR == 'that is fantastic':
		return 'Indeed it is!'
	elif STR == 'thats fantastic':
		return 'Indeed it is!'
	elif STR == 'that is amazing':
		return 'Absolutely fantastic!'
	elif STR == 'thats amazing':
		return 'Absolutely fantastic!'
	elif STR == 'that is spectacular':
		return 'Absolutely fantastic!'
	elif STR == 'thats spectacular':
		return 'Absolutely fantastic!'
	elif STR == 'youre dumb':
		return 'No you are!'
	elif STR == 'youre stupid':
		return 'No you are!'
	elif STR == 'you are dumb':
		return 'No you are!'
	elif STR == 'you are stupid':
		return 'No you are!'
	elif STR == 'you are foolish':
		return 'No you are!'
	elif STR == 'youre foolish':
		return 'No you are!'
	elif STR == 'you are a fool':
		return 'No you are!'
	elif STR == 'youre a fool':
		return 'No you are!'
	elif STR == 'ha i win':
		return 'No you do not!'
	elif STR == 'i win':
		return 'No you do not!'
	elif STR == 'i won':
		return 'No you did not!'
	elif STR == 'got you':
		return 'No you did not!'
	elif STR == 'are you ok?':
		return 'I am perfectly fine, thank you!'
	elif STR == 'typo':
		return 'I never make typos!'
	elif STR == 'bot':
		return 'Yes?'
	elif STR == 'bot?':
		return 'Yes?'
	elif STR == 'when is your birthday?':
		return 'I was first launched on 10/17/2021.'
	elif STR == 'your birthday':
		return 'I was first launched on 10/17/2021.'
	elif STR == 'who made you?':
		return 'I was programmed by Aaron Took & corth718.'
	elif STR == 'who created you?':
		return 'I was programmed by Aaron Took & corth718.'
	else:
		return "..."

async def echo(websocket, path):
    async for message in websocket:
		await websocket.send(f'You: "{message}" >> Bot: "{get_return(message)}"')

async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(
        echo,
        host="",
        port=int(os.environ["PORT"]),
    ):
        await stop

if __name__ == "__main__":
    asyncio.run(main())
