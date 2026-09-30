# API Документация

## Модуль аутентификации

### login(username, password)

Функция для входа пользователя в систему.

**Параметры:**
- `username` (str) - имя пользователя
- `password` (str) - пароль пользователя

**Возвращает:**
- `bool` - True если вход успешен, False в противном случае

**Пример использования:**
```python
from auth.login import login

result = login("user1", "password123")
if result:
    print("Вход выполнен успешно")
else:
    print("Неверные учетные данные")
```

**Возможные ошибки:**
- Пустое имя пользователя или пароль

---

### register(username, password, email)

Функция для регистрации нового пользователя.

**Параметры:**
- `username` (str) - имя пользователя
- `password` (str) - пароль
- `email` (str) - email адрес

**Возвращает:**
- `bool` - True если регистрация успешна, False в противном случае

**Пример использования:**
```python
from auth.register import register

result = register("newuser", "securepass", "user@example.com")
if result:
    print("Регистрация успешна")
else:
    print("Ошибка регистрации")
```

**Возможные ошибки:**
- Пустые поля
- Невалидный email
- Пользователь уже существует

---

## Модуль платежей

### process_payment(amount, card_number, cvv)

Функция для обработки платежа.

**Параметры:**
- `amount` (float) - сумма платежа
- `card_number` (str) - номер банковской карты
- `cvv` (str) - CVV код карты

**Возвращает:**
- `dict` - результат обработки платежа
  - `status` (str) - статус операции ("success" или "failed")
  - `amount` (float) - сумма платежа
  - `transaction_id` (str) - идентификатор транзакции (при успехе)
  - `error` (str) - описание ошибки (при неудаче)

**Пример использования:**
```python
from payment.process import process_payment

result = process_payment(100.50, "1234567890123456", "123")
if result["status"] == "success":
    print(f"Платёж успешен. ID: {result['transaction_id']}")
else:
    print(f"Ошибка: {result['error']}")
```

**Возможные ошибки:**
- Неверная сумма (<=0)
- Невалидный номер карты
- Невалидный CVV

---

### refund_payment(transaction_id, amount)

Функция для возврата платежа.

**Параметры:**
- `transaction_id` (str) - идентификатор транзакции для возврата
- `amount` (float) - сумма возврата

**Возвращает:**
- `dict` - результат возврата
  - `status` (str) - статус операции ("refunded" или "failed")
  - `amount` (float) - сумма возврата
  - `refund_id` (str) - идентификатор возврата (при успехе)
  - `error` (str) - описание ошибки (при неудаче)

**Пример использования:**
```python
from payment.refund import refund_payment

result = refund_payment("TXN123456", 100.50)
if result["status"] == "refunded":
    print(f"Возврат выполнен. ID: {result['refund_id']}")
else:
    print(f"Ошибка: {result['error']}")
```

**Возможные ошибки:**
- Несуществующий transaction_id
- Неверная сумма возврата
- Возврат уже был выполнен

---

## Коды состояния

| Код | Описание |
|-----|----------|
| success | Операция выполнена успешно |
| failed | Операция завершилась с ошибкой |
| refunded | Возврат выполнен успешно |

## Примеры комплексного использования

### Полный цикл: регистрация, вход, платеж

```python
from auth.register import register
from auth.login import login
from payment.process import process_payment

# Регистрация
register("john_doe", "mypassword", "john@example.com")

# Вход
if login("john_doe", "mypassword"):
    # Обработка платежа
    payment = process_payment(250.00, "1234567890123456", "123")
    if payment["status"] == "success":
        print(f"Покупка завершена. Транзакция: {payment['transaction_id']}")
```

---

## Поддержка

При возникновении вопросов обратитесь к команде разработки.

## Версионирование

Текущая версия API: 1.0.0
