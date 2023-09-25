from dataclasses import dataclass, field

@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)

# But let's imagine that we need to form a calculated 
# property in some class, for example, Vector3D during 
# initialization:

# class Vector3D:
#     def __init__(self, x: int, y: int, z: int):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.length = (x * x + y * y + z * z) ** 0.5

# Here the local length attribute is calculated based 
# on the parameters x, y, z. How can this be done when 
# declaring Data Classes?

# Method __post_init__()

@dataclass
class V3D:
    x: int
    y: int
    z: int
 
    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

v = V3D(1, 2, 3)
print(v)
# V3D(x=1, y=2, z=3)

print(v.__dict__)
# {'x': 1, 'y': 2, 'z': 3, 'length': 3.7416573867739413}

# But then why is it not output by the repr() function? 
# The fact is that the magic method __repr__() outputs 
# only those attributes that were specified when declaring 
# the class. All the others that are created during the 
# formation of the object are not taken into account in 
# the __repr__() method. How then to get out of this 
# situation and specify that the local length attribute 
# should also be displayed? Very simple! Let's specify 
# this attribute when declaring a class with a little 
# refinement:

@dataclass
class V3D:
    x: int
    y: int
    z: int
    length: float = field(init=False)
 
    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

v = V3D(1, 2, 3)
print(v)
# V3D(x=1, y=2, z=3, length=3.7416573867739413)

# Field() function

# In general, the field() function provides rich functionality for managing 
# declared attributes in Data Classes. We saw how its two parameters work: 
# init and default_factory. Quite often you can find the use of three more:

# repr – boolean value True/False indicates whether to use the attribute in 
# the magic method __repr__() (by default True);
# compare – boolean value True/False indicates whether to use the attribute 
# when comparing objects (by default True);
# default – default value (initial value).
# Their meaning is quite clear. Let's exclude the x attribute from the __repr__() 
# method and from the comparison operations the z and length attributes. 
# We get the following class declaration:

@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    length: float = field(init=False, compare=False)
 
    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

# Then when displaying and comparing two objects:

v = V3D(1, 2, 3)
v2 = V3D(1, 2, 5)
print(v)
print(v == v2)

# we will see only three attributes: y, z, length and the result is True, 
# because the x, y coordinates of objects v and v2 coincide.

# The rest of the parameters of the field() function can be found on the 
# official documentation page:

# https://docs.python.org/3/library/dataclasses.html

# Declaring parameters of the InitVar type
# Let's now assume that we would like to calculate the length of a vector 
# depending on the value of some parameter, for example, calc_len. When 
# describing a regular initializer , this could be done as follows:

class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0

# And how to do this when declaring Data Classes? To determine the parameters 
# involved in initialization (such as calc_len), there is a special class of 
# the InitVar type in the dataclasses module:

from dataclasses import dataclass, field, InitVar

# If an attribute is annotated with this class during the declaration, 
# it is automatically passed as a parameter to the __post_init__() method 
# so that it can be used when forming calculated properties:

@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)
 
    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

# Note that I have added the default=0 parameter to the field() function 
# here for the length attribute. That is, the initial value of the length 
# attribute is zero. If the calc_len parameter is True, then the __post_init__() 
# method will recalculate and generate a new value of the local length attribute.

# Parameters of the dataclass decorator
# So far, we have used the dataclass decorator with default parameters. 
# However, various arguments can be passed to it and the process of 
# forming the final class can be controlled. Here are the main parameters 
# that the dataclass decorator accepts.

# Parameter

# Description

# init = [True | False]

# Takes a Boolean value, by default True. If the value is True, the 
# initializer is declared in the class, otherwise it is not declared.

# repr = [True | False]

# Takes a Boolean value, by default True. If the value is True, the 
# magic method __repr__() is declared in the class, otherwise it is 
# not declared.

# eq = [True | False]

# Takes a Boolean value, by default True. If the value is True, then 
# the magic method __eq__() is declared in the class, otherwise it is 
# not declared.

# order = [True | False]

# Takes a Boolean value, False by default. If the value is True, then 
# magic methods for comparison operations are declared in the class 
# <; <=; >; >=, otherwise, they are not announced.

# unsafe_hash = [True | False]

# Affects the formation of the magic method __hash__()

# frozen = [True | False]

# Takes a Boolean value, False by default. If the value is True, then 
# the attributes of the class objects become unchanged (you can only 
# initialize once in the initializer).

# slots = [True | False]

# Takes a Boolean value, False by default. If True, the attributes 
# are declared in the __slots__ collection.

# There are other parameters of the dataclass decorator. You can read 
# more about them on the official documentation page:

# https://docs.python.org/3/library/dataclasses.html

# Let's look at the main ones sequentially. The first parameters init, 
# repr, eq, I think, are clear. If the argument init=False is passed 
# to the decorator:

# @dataclass(init=False)
# then the class will be formed without its own initializer 
# (the initializer of the base class will be used). As a result, 
# we will not be able to create an object with the transmission of 
# argument values:

# v = V3D(1, 2, 3, False)
# This is useful when all the described attributes take default 
# values and they are not supposed to be immediately redefined in 
# the initializer. For example, if the class will later be used as 
# a base for building other child classes.

# Next parameter:

# @dataclass(repr=False)
# prohibits the formation of the magic method __repr__() inside the 
# current class. As a result, a similar method of the base class 
# will be used. This is easy to see if you create an object and 
# output it to the console:

v = V3D(1, 2, 3, False)
print(v)
# We will see something similar to:

# <__main__.V3D object at 0x00000236FAD67D50>

# By analogy, the eq parameter works:

# @dataclass(repr=False, eq=False)
# It prohibits the formation of its own magic method __eq__() 
# for comparing objects with each other for equality. Now 
# objects are compared by their identifiers, and since they 
# are different, when comparing:

v = V3D(1, 2, 3, False)
v2 = V3D(1, 2, 3)
print(v == v2)
# we get the value False.

# The following order parameter can only be set to True in 
# conjunction with eq=True. For example, the following line 
# will result in an error:

# @dataclass(eq=False, order=True)
# Therefore, we need to either remove the eq parameter 
# (by default it is True), or explicitly set it to True:

# @dataclass(eq=True, order=True)
# I think you guessed why? Comparison operations for greater 
# than or equal to, less than or equal to use the magic method 
# __eq__(). Therefore, he must be present.

# So, after enabling the order parameter, we have the opportunity 
# to compare objects of the class by more, less and more or equal 
# and less or equal:

@dataclass(eq=True, order=True)
class V3D:
    x: int
    y: int
    z: int
 
 
v = V3D(1, 2, 5)
v2 = V3D(1, 2, 3)
 
print(v < v2)  # False
print(v > v2)  # True
# The comparison is performed at the level of tuples containing 
# attribute values (x, y, z) in the order of their declaration in 
# the class. In this case, there is a sequential comparison first 
# of the values of x with each other, then, y and then - z. As soon 
# as a pair is found for which the value True or False can be 
# calculated, the check is completed. In fact, in the given example, 
# only the last numbers 5 and 3 are compared with each other, the 
# rest are equal, so the < and> operations skip them.

# If we need to exclude any attributes from comparison operations, 
# then, as I have already noted, we should use the field() function 
# for this and exclude the corresponding field in it through the 
# compare parameter:

@dataclass(eq=True, order=True)
class V3D:
    x: int = field(compare=False)
    y: int
    z: int
# Now objects will be compared only by two local attributes y and z.

# Here you should pay attention to the fact that if any 
# comparison method is declared in the class to be greater, 
# less, or greater than or equal to or less than or equal to, 
# then a TypeError exception will occur:

@dataclass(order=True)
class V3D:
    x: int = field(compare=False)
    y: int
    z: int
 
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
# The last parameter that we will consider is frozen, 
# which allows you to "freeze" the values of class attributes. 
# For example:

@dataclass(frozen=True)
class V3D:
    x: int
    y: int
    z: int
 
 
v = V3D(1, 2, 3)
print(v)
v.x = 5
# Will result in an error in the last line, 
# because it is impossible to change local attributes 
# when frozen=True in objects of the class.
