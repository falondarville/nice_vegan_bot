# follow-along with https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

import os
import time
import re
from slackclient import SlackClient

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# insert after the bot is started up
veganbot_id = None

RTM_READ_DELAY = 1 
EXAMPLE_COMMAND = 'do'
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

# parse events from Slack RTM API to locate bot commands
def parse_bot_commands(slack_events):
	for event in slack_events:
		if event['type'] == 'message' and not 'subtype' in event:
			user_id, message = parse_direct_mention(event['text'])
			if user_id == veganbot_id:
				return (message, event['channel'])
	return (None, None)

# locates direct mentions and returns user ID of mentioned
def parse_direct_mention(message_text):
	matches = re.search(MENTION_REGEX, message_text)
	return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

# executes bot command
def handle_command(command, channel):
	# default response
	default_response = f'Sorry there. Not sure what you mean. Try {EXAMPLE_COMMAND}'

	# find and executes the command
	response = None
	if command.startswith(EXAMPLE_COMMAND):
		response = 'Sure...'

	# sends the response back to the channel
	slack_client.api_call(
		'chat.postMessage',
		channel=channel,
		text=response or default_response
		)

if __name__ == '__main__':
	if slack_client.rtm_connect(with_team_state=False):
		print('Nice Vegan Bot is connected and running!')
		veganbot_id = slack_client.api_call('auth.test')['user_id']
		while True:
			command, channel = parse_bot_commands(slack_client.rtm_read())
			if command:
				handle_command(command, channel)
			time.sleep(RTM_READ_DELAY)
	else:
		print('Connection failed. Exception traceback printed above.')

