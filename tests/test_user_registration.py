import string
import random
import pytest
from model.user import User


def random_string(minlen, maxlen, suffix):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(minlen, maxlen))]) + suffix


def random_numeric_string(minlen, maxlen):
    symbols = "1234567890"
    return [random.choice(symbols) for i in range(random.randrange(minlen, maxlen))]


testdata = User(firstname=random_string(3, 5, "name"), lastname=random_string(3, 6, "surname"),
                address1=random_string(3, 6, "addr"),
                city=random_string(2, 3, ":city"), email=random_string(2, 7, "@test.com"),
                password=random_string(3, 6, "!"),
                phone=random_numeric_string(9, 10), postcode=(random_numeric_string(5, 6)), country="Albania")


@pytest.mark.parametrize("user", [testdata])
def test_user_registration(app, user):
    app.admin_panel.switch_off_catpcha()
    app.store_front.navigate_to_litecart_shop()
    app.user.create_account(user)
    app.user.logout()
    app.user.user(user)
    app.user.logout()
