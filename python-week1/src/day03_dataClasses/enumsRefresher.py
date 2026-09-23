from enum import Enum, auto, IntEnum

class Department(Enum):
    ENGINEERING = "engineering"
    MARKETING = "marketing"
    FINANCE = "finance"
    HR = "hr"


dept = Department.ENGINEERING

print(dept.name, dept.value) # - ENGINEERING  engineering

# Iteration
for dept in Department:
    print(dept.value)

"""
auto, IntEnum, IntFlag, Flag, etc. are the next pieces of Python's enum module
"""

# With auto(), Python generates the values for you
class Status(Enum):
    PENDING = auto()
    ACTIVE = auto()
    CLOSED = auto()

print(Status.PENDING.value, Status.ACTIVE.value, Status.CLOSED.value) # 1 2 3

# IntEnum

class Priority(Enum):
    LOW = 1
    HIGH = 2

print(Priority.HIGH.value == 2)

# Instead of doing this for integers, we can use IntEnum

class PriorityInt(IntEnum):
    LOW = 1
    HIGH = 2

print(PriorityInt.HIGH == 2)