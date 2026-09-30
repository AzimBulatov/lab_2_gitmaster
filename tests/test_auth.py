"""
Тесты для модуля аутентификации
"""

import sys
sys.path.append('../src')

from auth.login import login
from auth.register import register


def test_login():
    """Тест функции login"""
    assert login("user1", "password123") == True
    assert login("", "") == False
    print("Тесты login пройдены успешно")


def test_register():
    """Тест функции register"""
    assert register("user1", "password123", "user1@example.com") == True
    assert register("", "", "") == False
    print("Тесты register пройдены успешно")


if __name__ == "__main__":
    test_login()
    test_register()
    print("Все тесты пройдены!")
