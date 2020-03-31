import requests # Requests modülü import edildi
import json
import telegram
import time

bot = telegram.Bot(token="<TELEGRAM TOKEN>")

base_currency = 1000

while True:
    sonuc = requests.get(
        f"https://api.collectapi.com/economy/currencyToAll?int={base_currency}&base=TRY",
        
        headers={
            "content-type": "application/json",
            "authorization": "apikey <COLLECT API KEY>"
        }
    )

    json = sonuc.json()
    success = json["success"]
    results = json["result"]["data"] # List

    for result in results: # For döngüsü ile listenin her elemanı sırayla result değişkenine atandı
        if result["code"] == "USD": # Eğer listede sıradaki eleman dolarsa işlem yapılacak
            calculated_dollar = result["calculated"] # Number <float>
            string = result["calculatedstr"] # String

            print("$" + string) # $123.45

            # print(result["calculated"])
            # print(result["calculatedstr"])

    if calculated_dollar > base_currency:
        bot.send_message("<TELEGRAM CHAT ID>", f"{str(base_currency)} €'nun karşılığı {str(calculated_dollar)} $'dır")
    time.sleep(30) # 30 saniye bekliyoruz

# print(results[0]) # Listedeki ilk eleman
# print(len(json)) # 2
# print(success) # True
# print(len(results)) # 167
# print(sonuc) # 200 Object
# print(sonuc.text) # String
# print(sonuc.json()) # JSON Object
# print(json) # JSON Object
# print(json.dumps(sonuc.json())) # String