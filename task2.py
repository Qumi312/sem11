"""
Создайте класс Архив,
который хранит пару свойств.
Например, число и строку. При нового экземпляра класса,
старые данные из ранее созданных экземпляров сохраняются
в пару списков-архивов,
которые также являются свойствами экземпляра.
"""
class Data_:
    _instance = None
    def __init__(self, text ,name):
        self.text = text,
        self.name = name

    def __new__(cls, text, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.all_text = []
            cls._instance.all_name = []
        else:
            cls._instance.all_text.append(cls._instance.text)
            cls._instance.all_name.append(cls._instance.name)
        return cls._instance

    def __init__(self, name: str, text):
        self.name = name
        self.text = text


if __name__ == '__main__':
    c = Data_('Heghffghfghfghgfhdghdydtrhllo' , 'Joe')
    d = Data_('Hellhfgfghfco' , 'fgds')
    b = Data_('Hellftghdrfto' , 'yhugkjkkjyuf')
    print(f'{b = }, {b.all_text = }, {type(b)}')
    print(f'{c = }, {c.all_text = }, {type(c)}')
    print(f'{d = }, {d.all_text = }, {type(d)}')