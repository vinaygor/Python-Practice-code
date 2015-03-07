text = "X-DSPAM-Confidence:    0.8475";
firstpos=text.find('0');
print firstpos
Str= text[firstpos:]
number=float(Str)
print number