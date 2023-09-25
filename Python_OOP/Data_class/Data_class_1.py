# class Thing:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price

# t = Thing("Python Tutorial", 100, 1024)
# print(t)

from dataclasses import dataclass, field

@dataclass
class ThingData:
    name: str
    weight: int
    price: float

from pprint import pprint

pprint(ThingData.__dict__)
# mappingproxy({'__annotations__': {'name': <class 'str'>,
#                                   'price': <class 'float'>,
#                                   'weight': <class 'int'>},
#               '__dataclass_fields__': {'name': Field(name='name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x00000208362E6040>,default_factory=<dataclasses._MISSING_TYPE object at 0x00000208362E6040>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD),
#                                        'price': Field(name='price',type=<class 'float'>,default=<dataclasses._MISSING_TYPE object at 0x00000208362E6040>,default_factory=<dataclasses._MISSING_TYPE object at 0x00000208362E6040>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD),
#                                        'weight': Field(name='weight',type=<class 'int'>,default=<dataclasses._MISSING_TYPE object at 0x00000208362E6040>,default_factory=<dataclasses._MISSING_TYPE object at 0x00000208362E6040>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)},
#               '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False),
#               '__dict__': <attribute '__dict__' of 'ThingData' objects>,   
#               '__doc__': 'ThingData(name: str, weight: int, price: float)',              '__eq__': <function __create_fn__.<locals>.__eq__ at 0x00000208366C8AF0>,
#               '__hash__': None,
#               '__init__': <function __create_fn__.<locals>.__init__ at 0x00000208366C8940>,
#               '__module__': '__main__',
#               '__repr__': <function __create_fn__.<locals>.__repr__ at 0x00000208366C88B0>,
#               '__weakref__': <attribute '__weakref__' of 'ThingData' objects>})

td = ThingData("Python tutorial", 100, 1024)

print(td.name)
# Python tutorial
print(td)
# ThingData(name='Python tutorial', weight=100, price=1024)

td2 = ThingData("Python OOP", 80, 512)

print(td == td2)
# False

td3 = ThingData("Python OOP", 80, 512)

print(td2 == td3)
# True
# (name, weight, price) == (name, weight, price)

@dataclass
class ThingData:
    name: str
    weight: int
    price: float
 
    def __eq__(self, other):
        return self.weight == other.weight

td_2 = ThingData("Python OOP", 80, 640)
td_3 = ThingData("Python OOP 2", 80, 512)
print(td_2 == td_3)
# True

@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0

td = ThingData("Python tutorial", 100)
print(td)
# ThingData(name='Python tutorial', weight=100, price=0)

@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)

td = ThingData("Python tutorial", 100, 512)
print(td)
# ThingData(name='Python tutorial', weight=100, price=512, dims=[])
