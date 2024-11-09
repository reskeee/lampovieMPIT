from g4f.client import Client

client = Client()

def summarize(text_for_sum: str) -> str:
	global client
	prompt = "Составь краткий пересказ этого текста: {text_for_sum}"
	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[{"role": "user", "content": prompt}]
		)
	return response.choices[0].message.content

if __name__ == "__main__":
	file = open("scripts/text.txt").read().replace('\n', " ")
	print(summarize(file))
