import sys

def valid_email(line):
    line = line.strip().lower()
    if line.count("@") == 1:
        return line

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    emails = set()

    with open(input_file) as f:
        for line in f:
            email = valid_email(line)
            if email:
                emails.add(email)

    with open(output_file, "w") as f:
        for email in sorted(emails):
            f.write(email, "\n")


    # at = 0

    # with open("dane/emails.txt") as f:
    #     for line in f:
    #         for znak in line:
    #             if znak == "@":
    #                 at += 1
    #                 if at == 1:
    #                      emaile.add(line.lower())
    #
    #      #print(emaile)
    #     for email in sorted(emaile):
    #         print(email, end="")

else:
    print = ("Nieprawidlowa ilosc parametrow")