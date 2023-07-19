from tokenizer import VoiceBpeTokenizer
import nltk
nltk.download('punkt')

tokenizer = VoiceBpeTokenizer()

def calculate_token_count(text):
    input_text = text.strip()
    tokens = tokenizer.encode(input_text)
    return len(tokens)

with open('long.txt', 'r') as f:
    text = f.read().replace("\n", ' ').replace(';', '.')
sent = nltk.sent_tokenize(text)
result = ''
cur_sent_token_count = 0

for txt in sent:
    txt = txt.strip()
    token_count = calculate_token_count(txt)
    if token_count > 370:
        print("**** WARNING *** You have a sentence that is TOO LONG!")
        print(txt)
    if cur_sent_token_count + token_count > 370:
        # print(f"G: {txt}")
        cur_sent_token_count = token_count
        result += "\n" + txt + ' '
    else:
        # print(f"L: {txt}")
        cur_sent_token_count += token_count
        result += txt + ' '

with open('long_res.txt', 'w') as f:
    f.write(result.strip())
