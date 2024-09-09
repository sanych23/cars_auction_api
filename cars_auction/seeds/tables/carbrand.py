from magazine.models import CarBrand


class CarbrandSeed:
    model = CarBrand
    data = [
        {
            "id": 1,
            "name": "BMW",
            "logo": None,
            "description": "Bayerish Motoren Werke, civilian sport car."
        },
        {
            "id": 2,
            "name": "MERCEDES",
            "logo": None,
            "description": "Comfortable bayerish auto."
        },
        {
            "id": 3,
            "name": "AUDI",
            "logo": None,
            "description": "Very reliable auto."
        },
    ]

    @staticmethod
    def order():
        return 1

    def __init__(self) -> None:
        model = self.model
        for item in self.data:
            model.objects.create(**item).save()


    @staticmethod
    def delete():
        CarBrand.objects.all().delete()