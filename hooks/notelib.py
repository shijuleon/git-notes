COMMIT_MESSAGE_PATH = '.git/COMMIT_EDITMSG'

def read_from_commit_message():
	with open(COMMIT_MESSAGE_PATH) as f:	
		content = f.read()
	return content

def write_to_commit_message(text):
	with open(COMMIT_MESSAGE_PATH, 'w') as f:	
		f.write(text)
