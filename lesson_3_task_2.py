from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "16", "+79999999999"),
    Smartphone("Samsung", "S20", "+79888888888"),
    Smartphone("Nokia", "A14", "+79777777777")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
