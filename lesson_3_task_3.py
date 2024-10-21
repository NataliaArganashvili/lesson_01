from address import Address
from mailing import Mailing

address1 = Address("34566676", "Moscow", "Arbat", "25", "175")
address2 = Address("45678876", "Moscow", "Rublevka", "35", "165")
mailing = Mailing(adress1, adress2, 100, "567890")

print(f"Отправление {mailing.track} из {address1} в {address2}. Стоимость {mailing.cost} рублей.")
