user_last_login = {}
user_total_time = {}
with open("dane/logs.txt") as f:
    for line in f:
        login, action, time = line.split(";")
        time = int(time)
        if action == "LOGIN":
            user_last_login[login] = time
        if action == "LOGOUT":
            #print(user_last_login)
            #print(time - user_last_login[login])
            user_total_time[login] = user_total_time.get(login,0) + time - user_last_login[login]


#wersja 1
print("Czas przebywania w systemie")
for login in user_total_time:
    print("- ", login, ":", user_total_time[login], "s")


#wresja 2
def sort_key(x):
    return x[1]
print("Czas przebywania w systemie")
for item in sorted(user_total_time.items(), key=sort_key(), reverse=True):
    print(item)


#werasja 3
print("Czas przebywania w systemie")
for item in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
    print(item)

