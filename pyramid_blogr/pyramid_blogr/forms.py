from wtforms import (
    Form,
    StringField,
    TextAreaField,
    validators,
    IntegerField,
    PasswordField,
)
from wtforms.widgets import HiddenInput

strip_filter = lambda x: x.strip() if x else None


class BlogCreateForm(Form):
    """Assigned the form fields of blog record. """
    title = StringField('Заголовок, (Куплю шрот подсолнечника)',
                        [validators.length(min=10, max=60)],
                        filters=[strip_filter])
    amount = StringField('Объем поставки, (40 тонн)',
                         [validators.length(min=2, max=20)],
                         filters=[strip_filter])
    price = StringField('Цена, (5000 грн/т, 178.23 долл/т)',
                         [validators.length(min=3, max=20)],
                         filters=[strip_filter])
    vat = StringField('Статус по НДС: производитель, трейдер, экспотер и т.п.',
                      [validators.length(min=5, max=30)],
                      filters=[strip_filter])
    delivery_terms = StringField('Условия поставки Инкотермс (EXW, DAP, FCA..)',
                                 [validators.length(min=3)],
                                 filters=[strip_filter])
    address_delivery = TextAreaField('Адрес или место поставки \
(область, район, насел пункт, хозяйство/элеватор/порт-терминал/переход и т.п.)',
                                    [validators.length(min=30)],
                                    filters=[strip_filter])
    body = TextAreaField('Детали и подробности \
(протеин-42%, влажность-5%, любая форма расчета...)',
                        [validators.length(max=155)],
                        filters=[strip_filter])

class BlogUpdateForm(BlogCreateForm):
    id = IntegerField(widget=HiddenInput())


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=255)],
                           filters=[strip_filter])
    password = PasswordField('Password', [validators.Length(min=3)])
