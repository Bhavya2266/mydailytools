import todo_list
import password_generator
import currency_converter
import weather_forecast


print("press 1 for todo list")
print("press 3 for password generator")
print("press 2 for currency converter")
print("press 4 for weather forecast") 

inp=int(input("please choose a number between 1-4 : "))

if inp==1:
    print("welcome to todo_list")
    todo_list.main()
elif inp==2:
    print("welcome to currency_converter")
    currency_converter.main()
elif inp==3:
    print("welcome to password_generator")
    password_generator.main()
elif inp==4:
    print("welcome to weather_forecast")
    weather_forecast.main()
else:
    print("invalid pattern")

