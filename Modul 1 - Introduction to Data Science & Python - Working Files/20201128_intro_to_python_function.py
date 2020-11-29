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
    # try:
    email = str(email).lower()

    result = ""
    if email.count("@") == 1:
        if email.count(".") > 0:
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


print("*"*50)
print("andre@gmail.com: ", verify_email("andre@gmail.com"))
print("joni_12@yahoo.com: ", verify_email("joni_12@yahoo.com"))
print("andy34@city.id: ", verify_email("andy34@city.id"))
print("steve.roger_77@avengers01.space: ",
      verify_email("steve.roger_77@avengers01.space"))
print("*"*50)
print("andre254@gmail.com: ", verify_email("andre254@gmail.com"))
print("andre%^&@gmail.com: ", verify_email("andre%^&@gmail.com"))
print("john_capt@yah^^oo.com: ", verify_email("john_capt@yah^^oo.com"))
print("tony_stark@stark.corporation: ",
      verify_email("tony_stark@stark.corporation"))
print("Thor@@gmail.com: ", verify_email("Thor@@gmail.com"))
