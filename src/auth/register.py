"""
Модуль для регистрации новых пользователей
"""

def register(username, password, email):
    """
    Функция для регистрации нового пользователя
    
    Args:
        username (str): Имя пользователя
        password (str): Пароль
        email (str): Email адрес
        
    Returns:
        bool: True если регистрация успешна, False в противном случае
    """
    # Заглушка для демонстрации
    if username and password and email:
        print(f"Пользователь {username} успешно зарегистрирован с email {email}")
        return True
    return False
