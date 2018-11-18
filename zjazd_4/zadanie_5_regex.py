import re

#EMAIL_PATTERN = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") #pattern z netu
EMAIL_PATTERN = re.compile("[\w\.-]+@[\w+\.]")
DATE_PATTERN = re.compile("\d{2} \w{3} \d{4}")
POSTCODE_PATTERN = re.compile("^(\d{2}-\d{3}) | (\d{2}-\d{3}) | (\d{2}-d{3})$")

with open("input.txt") as f:
    data = f.read()
    print("Kody pocztowe" + " ".join(POSTCODE_PATTERN.findall(data)))
    print("emaile" + " ".join(EMAIL_PATTERN.findall(data)))
    print("emaile" + " ".join(DATE_PATTERN.findall(data)))