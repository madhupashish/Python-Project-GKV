import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# We are making Drink Water time reminder. Here we are taking initial time as input and after each hour or some time given by the user then we remind them
print("Enter the time to start the timer for Drink water reminder and here the time is in the format of 24 hours format ")
set_time_hour = int(input("Enter the hour to start :"))
set_time_min = int(input("Enter the minute to start :"))

s_hour_i = int(time.strftime("%H"))
s_min_i = int(time.strftime("%M"))
print(s_hour_i)
print(s_min_i)
print(set_time_hour)
print(set_time_min)

diff_sec = (set_time_hour-s_hour_i)*60*60 + (set_time_min-s_min_i)*60
time.sleep(diff_sec)
s_hour_f1 = int(time.strftiem("%H"))
s_min_f1 = int(time.strftime("%M"))


if s_hour_f1 == set_time_hour and s_min_f1 == set_time_min :
        speaker.speak("Time to Drink Water")
        continue_input = int(input("If you want to continue enter 1"))
        if continue_input == 1:
          s_hour_f2 = int(time.strftiem("%H"))
          s_min_f2 = int(time.strftime("%M"))
          
          while True:
               if s_hour_f == set_time_hour + 1 and s_min_f == set_time_min:
                    speaker.speak("Time to Drink Water")
                    keep_moving = int(input("If you want to continue the remainder enter 1 : "))
                    if keep_moving == 1:
                         continue
                    else:
                         break    
                    



