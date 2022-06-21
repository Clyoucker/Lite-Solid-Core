def command(text):
	text = text.lower().title().strip()
	while True:
		if " " in text: text = text.replace(" ", ".")
		else: break
	return text

def lowers(text):
	text = text.lower().strip()
	while True:
		if "  " in text: text = text.replace("  ", " ")
		else: break
	if text.startswith(""):
		return text
	else:
		text = "" + text
		return text