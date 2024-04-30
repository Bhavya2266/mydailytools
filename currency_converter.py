currencies = [
{ "currency": "USD", "name": "United States Dollar",
        "symbol": "$", "rate": 1.00
    },
    { "currency": "EUR","name": "Euro",
        "symbol": "€", "rate": 0.86
    }
    {"currency": "GBP","name": "Pound",
      "symbol": "£","rate": 0.72

    },
    {"currency": "JPY","name": "Yen",
       "symbol": "¥","rate": 110.81
    },
]

def printcurrency():
    print("Available currencies:")
    i = 1
    for currency in currencies:
        print(f"{i}. {currency['name']} ({currency['symbol']})")
        i += 1


def main():
    while True:
        printcurrency()
        source_currency = int(input("Choose the source currency (1-4): ")) - 1
        target_currency = int(input("Choose the target currency (1-4): ")) - 1
        if 0 <= source_currency < len(currencies) and 0 <= target_currency < len(currencies):
            break
        else:
            print("Invalid input. Please choose a valid currency.")
    
  
    inp=int(input("how much do you want to convert: "))
    conversion_rate = currencies[target_currency-1]["rate"] / currencies[source_currency-1]["rate"]
    converted_amount = inp*conversion_rate
    print("here is your currency", converted_amount)


if _name_ == "_main_":
    main()