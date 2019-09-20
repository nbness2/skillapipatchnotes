class BaseField:
    def __init__(self, field_name, field_description, field_value=None):
        self.field_name = field_name
        self.field_value = field_value
        self.field_description = field_description


class TextboxField(BaseField):
    def __init__(self, field_name, field_value, field_description, field_validator):
        BaseField.__init__(self, field_name, field_description)
        self.field_value = field_value
        self.field_validator = field_validator

    @property
    def value(self):
        return self.field_value

    @value.setter
    def value(self, field_value):
        if self.field_validator(field_value):
            self.field_value = field_value


class StringField(TextboxField):
    def __init__(self, field_name, field_value, field_description):
        TextboxField.__init__(self, field_name, field_value, field_description, lambda x: True)

class NumberField(TextboxField):
    def __init__(self, field_name, field_value: int, field_description):
        TextboxField.__init__(self, field_name, field_value, field_description, lambda x: x is int or x is float or x.isnumeric())


class ChoiceField(BaseField):
    def __init__(self, field_name, choices, field_description):
        BaseField.__init__(self, field_name, field_description)
        self.choices = choices
        self.choice_index = 0
        self.field_value = choices[0]


class BooleanChoiceField(ChoiceField):
    def __init__(self, field_name, field_description):
        ChoiceField.__init__(self, field_name, field_description, ["False", "True"])
