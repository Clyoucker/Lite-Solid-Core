def correcter(text):
	text = text.lower().title().strip()
	while True:
		if "  " in text:
			text = text.replace("  ", " ")
		else:
			break
	while True:
		if "//" in text:
			text = text.replace ("//","/")
		else:
			break
	if text.startswith("/"):
		return text
	else:
		text = "/" + text
		return text

def correcter_2(text):
	text = text.lower().title().strip()
	while True:
		if "  " in text:
			text = text.replace("  ", " ")
		else:
			break
	while True:
		if "/" in text:
			text = text.replace ("/","")
		else:
			break
	if text.startswith(""):
		return text
	else:
		text = "" + text
		return text