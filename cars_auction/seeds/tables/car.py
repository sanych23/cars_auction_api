from magazine.models import Car, CarBrand


class CarSeed:
    model = Car
    data = [
        {
            "item": {
                "name": "M5",
                "year": "2001-07-19",
                "classification": "Sedan",
                "description": "Sport civilian car",
                "price": 10000000,
            },
            "brand": "BMW",
        },
        {
            "item": {
                "name": "W124",
                "year": "1990-07-19",
                "classification": "Sedan",
                "description": "Very comfortable old car",
                "price": 150000,
            },
            "brand": "MERCEDES",
        },
        {
            "item": {
                "name": "RS6",
                "year": "2010-07-19",
                "classification": "Sedan",
                "description": "Most sport coupe car!",
                "price": 150000,
            },
            "brand": "AUDI",
        },
        {
            "item": {
                "name": "M760LI",
                "year": "2016-07-19",
                "classification": "Business",
                "description": "Very comfortable V12 car",
                "price": 150000,
            },
            "brand": "MERCEDES",
        },
    ]

    @staticmethod
    def order():
        return 2

    def __init__(self) -> None:
        model = self.model
        for item in self.data:
            item["item"]["car_brand"] = CarBrand.objects.get(name=item["brand"])
            model.objects.create(**item["item"]).save()


    @staticmethod
    def delete():
        Car.objects.all().delete()
