from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "16", "+79999999999"),
    Smartphone("Samsung", "S24", "+79888888888"),
    Smartphone("Nokia", "A14", "+79777777777"),
    Smartphone("Xiaomi", "ML", "+79771234567"),
    Smartphone("Nokia", "A14", "+79777654321")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
