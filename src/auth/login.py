"""
Модуль для аутентификации пользователей
"""

def login(username, password):
    """
    Функция для входа пользователя в систему
    
    Args:
        username (str): Имя пользователя
        password (str): Пароль
        
    Returns:
        bool: True если вход успешен, False в противном случае
    """
    # ИСПРАВЛЕНО: добавлена проверка на None
    if username and password and username != "" and password != "":
        print(f"Пользователь {username} успешно вошёл в систему")
        return True
    return False
