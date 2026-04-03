import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'(?i)#E91E63', '#A3485E', text)
text = re.sub(r'(?i)#FF9800', '#C26B4B', text)
text = re.sub(r'(?i)#F57C00', '#B05B3C', text)
text = re.sub(r'(?i)#9C27B0', '#724976', text)
text = re.sub(r'(?i)#03A9F4', '#4C8291', text)
text = re.sub(r'(?i)#FFF9F5', '#F9F6F4', text)
text = re.sub(r'rgba\(233,\s*30,\s*99,', 'rgba(163,72,94,', text)
text = re.sub(r'rgba\(156,\s*39,\s*176,', 'rgba(114,73,118,', text)
text = re.sub(r'rgba\(3,\s*169,\s*244,', 'rgba(76,130,145,', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Done editing colors!')
