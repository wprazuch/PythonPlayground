class Person:
    def __init__(self, name):
        self._name = name

    # Getter function
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):

    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPerson1(Person):

    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

# descriptor


class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict[self.name] = value


class Person2:
    name = String('name')

    def __init__(self, name):
        self.name = name


class SubPerson2(Person2):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print("Setting name to ", value)
        super(SubPerson2, SubPerson2).name = value

    @name.deleter
    def name(self):
        print("Deleting name")
        super(SubPerson2, SubPerson2).name.__delete__(self)
