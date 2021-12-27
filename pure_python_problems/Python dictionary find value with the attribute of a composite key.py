class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return self.age

    def __eq__(self, other):
        return isinstance(other, person) and other.age == self.age

    def __str__(self):
        return "name: " + self.name + " age: " + self.age


class find:
    def run(age):
        d = {obj("hi", 10): "one", obj("bye", 20): "two"}
        item = d.get(age, None)
        print(item)


if __name__ == "__main__":
    one = person("one", 1)
    two = person("two", 2)

    d = {one: "one", two: "two"}

    print(d.get(0, None))
    print(d.get(1, None))
    print(d.get(2, None))
