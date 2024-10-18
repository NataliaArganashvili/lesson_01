from adress import Adress
from mailing import Mailing

adress1 = Adress("34566676", "Moscow", "Arbat", "25", "175")
adress2 = Adress("45678876", "Moscow", "Rublevka", "35", "165")
mailing = Mailing(adress1, adress2, 100, "567890")

print(f"Отправление {mailing.track} из {adress1} в {adress2}. Стоимость {mailing.cost} рублей.")
