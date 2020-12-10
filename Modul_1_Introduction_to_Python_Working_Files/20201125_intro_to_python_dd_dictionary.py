Hari = {"senin": "monday",
        "selasa": "tuesday",
        "rabu": "wednesday",
        "kamis": "thursday",
        "jumat": "friday",
        "sabtu": "saturday",
        "minggu": "sunday"}

try:
    day_input = str(input("type a day: ")).lower()

    keys = list(Hari.keys())
    values = list(Hari.values())
    items = list(Hari.items())

    if day_input in keys:
        english_day = Hari[day_input]
        print(f"Hari '{day_input}' dalam bahasa inggris adalah '{english_day}'")
    else:
        indonesian_day = keys[values.index(day_input)]
        print(f"'{day_input}' in Indonesian is '{indonesian_day}'")


except:
    print("input should be days")
