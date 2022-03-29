def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1_map = {}
    s2_map = {}
    for e in s1:
        s1_map[e] = s1_map.get(e, 0) + 1
    for e in s1:
        s2_map[e] = s2_map.get(e, 0) + 1
    for e in s2:
        if e not in s1_map or s1_map[e] != s2_map[e]:
            return False

    return True


print(is_anagram("danger", "garden"))
print(is_anagram("danger", "gardenn"))


class AnimalA:
    def __init__(self, type: str):
        self.type = type


class AnimalB:
    type = "dog"


class AnimalC:
    type = "cat"

    def __init__(self, type: str):
        self.type = type


a = AnimalA("bird")
print(a.type)
print(AnimalB.type)
c = AnimalC("tiger")
print(c.type)
print(AnimalC.type)
