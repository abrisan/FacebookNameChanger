import os
from collections import Counter
from bs4 import BeautifulSoup

class FacebookNameChanger:
	def __init__(self):
		messages_path = os.path.join(
			os.getcwd(),
			"messages")

		print(messages_path)

		self.message_paths = [
			os.path.join(os.getcwd(), 'messages', path) 
			for path in os.listdir(messages_path)
			if path.split('.')[-1] == 'html'
		]

	def get_names(self, message_file):
		title = ''

		with open(message_file, 'r') as message_f:
			soup = BeautifulSoup(message_f)
			title = soup.title.string

		conversation_name = ''.join(title.split()[2:]) + '.html'

		return message_file, conversation_name

	def do_rename(self, old, new):
		os.rename(old, os.path.join(os.getcwd(), 'messages', new))

	def rename(self):
		if not self.message_paths:
			print('No messages')
			return

		print("Getting Names")
		names = [self.get_names(path) for path in self.message_paths]


		namesCounter = dict(Counter(x[1] for x in names))

		unique_id = 0

		print("Doing renames")
		for old, new in names:
			if namesCounter[new] > 1:
				self.do_rename(old, str(unique_id) + new)
				unique_id += 1
			else:
				self.do_rename(old, new)



if __name__ == "__main__":
	nc = FacebookNameChanger()
	nc.rename()