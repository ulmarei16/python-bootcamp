import random

print(random.random()) # zwroci losoqwa liczbe od 0 do 1

print(random.randint(1,101))
print(random.randrange(1,100))

pets = ["cat", "dog", "fish", "rabbit", "horse"]
print(random.choice(pets))


random.seed(3) # to spowoduje, że zawsze bedzie zawsze zwracal tę samą liczbe
print(random.random())