def timeConverter(input_second):
    try:
        n_hour = 3600
        n_minute = 60

        if type(input_second) == int:
            if 0 <= input_second <= 359999:
                # Calculation Part
                hour = input_second // n_hour
                seconds_mod = input_second % n_hour

                minute = seconds_mod // n_minute
                seconds_mod = seconds_mod % n_minute

                second = seconds_mod

                # Display Part
                time = []

                if hour < 10:
                    hour_0 = "0" + str(hour)
                    time.append(hour_0)
                else:
                    time.append(hour)

                if minute < 10:
                    minute_0 = "0" + str(minute)
                    time.append(minute_0)
                else:
                    time.append(minute)

                if second < 10:
                    second_0 = "0" + str(second)
                    time.append(second_0)
                else:
                    time.append(second)

                output = f"Convertion: {time[0]}:{time[1]}:{time[2]}"

                return output
            else:
                return 'Invalid Input!'
        else:
            return 'Invalid Input!'
    except:
        return 'Invalid Input'


# This is only to display the result
def print_time_converter(input):
    output = timeConverter(input)
    print(f"{input} \t --> {output}")


time1 = 3600
time2 = 3665
time3 = 359999
time3a = 360000
time4 = 498909
time5 = -18900
time6 = 20.5
time7 = 'ujian'

print_time_converter(time1)
print_time_converter(time2)
print_time_converter(time3)
print_time_converter(time3a)
print_time_converter(time4)
print_time_converter(time5)
print_time_converter(time6)
print_time_converter(time7)
