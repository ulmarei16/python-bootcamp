import re
pattern = re.compile("\d{3}-\d{3}-\d{3}")  #<--podajemy tu przepis
text = "1-2-3"
text2 = "111-223-444-333-444-555  333-444-555"

print(pattern.findall(text)) #<-- szuka wszystkich rzeczy z wyrazeniem ze wzroru
print(pattern.findall(text2))
