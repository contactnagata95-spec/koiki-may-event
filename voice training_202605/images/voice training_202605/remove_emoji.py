import io

with io.open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('🎤 ', '')
text = text.replace('🎤', '')
text = text.replace('❣', '！')

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Replaced emojis correctly!')
