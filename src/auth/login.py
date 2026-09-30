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
    # Заглушка для демонстрации
    if username and password:
        print(f"Пользователь {username} успешно вошёл в систему")
        return True
    return False
