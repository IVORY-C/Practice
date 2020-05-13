from main.shared import base_class as bc
from main.use_cases import josephus as jsp


reader = []
reader.append(bc.Person('Morty', 12, 'male'))
reader.append(bc.Person('Rick', 53, 'male'))
reader.append(bc.Person('Summer', 16, 'female'))
reader.append(bc.Person('Beth', 34, 'female'))
reader.append(bc.Person('Jerry', 36, 'male'))

ring = jsp.Ring(reader)
ring.start = 2
ring.step = 5
ring.reset()

result = []
for item in ring:
    result.append(item.name)

assert result == ['Rick', 'Summer', 'Jerry', 'Morty', 'Beth']