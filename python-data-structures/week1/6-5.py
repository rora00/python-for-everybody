text = "X-DSPAM-Confidence:    0.8475"
startpos = text.find('0')
num = text[startpos:]
print(float(num))