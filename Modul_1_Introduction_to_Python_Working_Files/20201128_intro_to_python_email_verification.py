# email verification
# - buat sebuah return function dengan 1 argumen untuk mengecek/memvalidasi email

# input: masukkan email:

# kondisi:
# email valid jika:
# - memiliki format nama user@nama hosting.ekstensi
# - nama user hanya boleh huruf, angka, underscore(_) dan dot (.)
# - nama hosting hanya boleh huruf dan angka
# - nama ekstensi hanya boleh huruf dan maksimal 5 karakter

# output:
# alamat email yang anda masukkan valid!!
# jika tidak valid, keluar alasannya:
# format email salah (misal tidak ada @ atau tidak ada .ekstensi)
# format username yang anda masukkan salah
# format hosting yang anda masukkan salah
# format ekstensi yang anda masukkan salah

# contoh email
# valid: andre@gmail.com, joni_12@yahoo.com, andy34@city.id, steve.roger_77@avengers01.space
# invalid: andre254@gmail.com, andre%^&@gmail.com, john_capt@yah^^oo.com, tony_stark@stark.corporation, Thor@@gmail.com

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                      'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters = ["_", ".", "@"]
characters = alphabet + number + special_characters


def verify_email(email):
    email = str(email).lower()

    result = ""
    index_at = ""
    if email.count("@") == 1 and email[0] != "@":
        index_at = email.index("@")
        if email[:index_at].isalnum:
            if email.count(".") > 0:
                # looking index from the end of list
                dot_index = ~email[::-1].index(".")

                if dot_index >= -6:
                    for i in email[-6:]:
                        if i in alphabet:
                            for i in email:
                                if i in characters:
                                    result = "email is valid"
                                else:
                                    result = "email not valid, email can only contain letters, numbers, '_', or '.'"
                                    break
                        else:
                            result = "email not valid, extension can be only letters"
                else:
                    result = "email not valid, extension should be no longer than 5 characters"
            else:
                result = "email not valid, email should contain extension preceded by '.'"
    else:
        result = "email not valid, pay attention to '@'"

    return result


def print_email_verification(email):
    result = verify_email(email)
    print(f"{email}: {result}")


email1 = "andre@gmail.com"
email2 = "joni_12@yahoo.com"
email3 = "andy34@city.id"
email4 = "steve.roger_77@avengers01.space"
email5 = "andre254@gmail"
email6 = "andre%^&@gmail.com"
email7 = "john_capt@yah^^oo.com"
email8 = "tony_stark@stark.corporation"
email9 = "Thor@@gmail.com"
email10 = "@gmail"

print_email_verification(email1)
print_email_verification(email2)
print_email_verification(email3)
print_email_verification(email4)
print_email_verification(email5)
print_email_verification(email6)
print_email_verification(email7)
print_email_verification(email8)
print_email_verification(email9)
print_email_verification(email10)

print_email_verification(email=input("type email: "))
