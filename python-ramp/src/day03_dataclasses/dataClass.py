"""
A decorator that generates boilerplate for classes that mainly hold data. 
You declare fields with type annotations; it writes __init__, __repr__, and __eq__ for you.
__repr__ is toString() in java
__eq__ for comparing class objects
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class InventoryItem:
    name : str
    price : int
    quantity: int = 0

    def total_cost(self):
        return self.price * self.quantity

#### For immutables like list, dict, set, instead of default value, we need to use field()

"""
field() is a function that lets you configure a single dataclass field beyond just its type and default.
You only reach for it when a plain = value isn't enough
"""

@dataclass
class Teams:
    members: list[str] = field(default_factory=list)
    tag: set[str] = field(default_factory=set)
    created_date: datetime = field(default_factory=datetime.now)

members = ['A','B']
team_1 = Teams(members, {'engineer','manager'})

print(team_1)

# repr and compare
# -- repr = false will avoid printing it in the description
@dataclass
class User:
    name: str
    api_key: str = field(repr=False)

u = User("ravi", "sk-secret123")
print(u)     # User(name='ravi') — key not shown

# compare=False — exclude from equality

@dataclass
class Document:
    content: str
    fetched_at: datetime = field(default_factory=datetime.now, compare=False)

d1 = Document("hello")
d2 = Document("hello")
print(d1 == d2)     # True — timestamps differ but aren't compared


### init=False — not a constructor argument, use for values computed and never wants to be passed
@dataclass
class Document:
    content: str
    word_count: int = field(init=False)

    def __post_init__(self):
        self.word_count = len(self.content.split())

d = Document("hello world foo")
print(d.word_count)     # 3