# Generated by Django 3.0.8 on 2020-07-28 00:45

from django.db import migrations
from django.apps import apps


BREEDS = {
    "affenpinscher": [],
    "african": [],
    "airedale": [],
    "akita": [],
    "appenzeller": [],
    "australian": [
        "shepherd"
    ],
    "basenji": [],
    "beagle": [],
    "bluetick": [],
    "borzoi": [],
    "bouvier": [],
    "boxer": [],
    "brabancon": [],
    "briard": [],
    "buhund": [
        "norwegian"
    ],
    "bulldog": [
        "boston",
        "english",
        "french"
    ],
    "bullterrier": [
        "staffordshire"
    ],
    "cairn": [],
    "cattledog": [
        "australian"
    ],
    "chihuahua": [],
    "chow": [],
    "clumber": [],
    "cockapoo": [],
    "collie": [
        "border"
    ],
    "coonhound": [],
    "corgi": [
        "cardigan"
    ],
    "cotondetulear": [],
    "dachshund": [],
    "dalmatian": [],
    "dane": [
        "great"
    ],
    "deerhound": [
        "scottish"
    ],
    "dhole": [],
    "dingo": [],
    "doberman": [],
    "elkhound": [
        "norwegian"
    ],
    "entlebucher": [],
    "eskimo": [],
    "finnish": [
        "lapphund"
    ],
    "frise": [
        "bichon"
    ],
    "germanshepherd": [],
    "greyhound": [
        "italian"
    ],
    "groenendael": [],
    "havanese": [],
    "hound": [
        "afghan",
        "basset",
        "blood",
        "english",
        "ibizan",
        "plott",
        "walker"
    ],
    "husky": [],
    "keeshond": [],
    "kelpie": [],
    "komondor": [],
    "kuvasz": [],
    "labrador": [],
    "leonberg": [],
    "lhasa": [],
    "malamute": [],
    "malinois": [],
    "maltese": [],
    "mastiff": [
        "bull",
        "english",
        "tibetan"
    ],
    "mexicanhairless": [],
    "mix": [],
    "mountain": [
        "bernese",
        "swiss"
    ],
    "newfoundland": [],
    "otterhound": [],
    "ovcharka": [
        "caucasian"
    ],
    "papillon": [],
    "pekinese": [],
    "pembroke": [],
    "pinscher": [
        "miniature"
    ],
    "pitbull": [],
    "pointer": [
        "german",
        "germanlonghair"
    ],
    "pomeranian": [],
    "poodle": [
        "miniature",
        "standard",
        "toy"
    ],
    "pug": [],
    "puggle": [],
    "pyrenees": [],
    "redbone": [],
    "retriever": [
        "chesapeake",
        "curly",
        "flatcoated",
        "golden"
    ],
    "ridgeback": [
        "rhodesian"
    ],
    "rottweiler": [],
    "saluki": [],
    "samoyed": [],
    "schipperke": [],
    "schnauzer": [
        "giant",
        "miniature"
    ],
    "setter": [
        "english",
        "gordon",
        "irish"
    ],
    "sheepdog": [
        "english",
        "shetland"
    ],
    "shiba": [],
    "shihtzu": [],
    "spaniel": [
        "blenheim",
        "brittany",
        "cocker",
        "irish",
        "japanese",
        "sussex",
        "welsh"
    ],
    "springer": [
        "english"
    ],
    "stbernard": [],
    "terrier": [
        "american",
        "australian",
        "bedlington",
        "border",
        "dandie",
        "fox",
        "irish",
        "kerryblue",
        "lakeland",
        "norfolk",
        "norwich",
        "patterdale",
        "russell",
        "scottish",
        "sealyham",
        "silky",
        "tibetan",
        "toy",
        "westhighland",
        "wheaten",
        "yorkshire"
    ],
    "vizsla": [],
    "waterdog": [
        "spanish"
    ],
    "weimaraner": [],
    "whippet": [],
    "wolfhound": [
        "irish"
    ]
}


def load_breeds(apps, schema_editor):
    """
    Loads the initial data for models Breed and Sub-Breed.
    """
    Breed = apps.get_model('customer', 'Breed')
    SubBreed = apps.get_model('customer', 'SubBreed')

    for breed, sub_breeds in BREEDS.items():
        obj = Breed.objects.create(name=breed)
        for sub_breed in sub_breeds:
            SubBreed.objects.create(name=sub_breed, breed=obj)


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_breeds),
    ]