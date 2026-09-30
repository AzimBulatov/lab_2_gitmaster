"""
Модуль для обработки платежей
"""

def process_payment(amount, card_number, cvv):
    """
    Функция для обработки платежа
    
    Args:
        amount (float): Сумма платежа
        card_number (str): Номер карты
        cvv (str): CVV код
        
    Returns:
        dict: Результат обработки платежа
    """
    if amount > 0 and card_number and cvv:
        print(f"Платёж на сумму {amount} обработан успешно")
        return {
            "status": "success",
            "amount": amount,
            "transaction_id": "TXN123456"
        }
    return {
        "status": "failed",
        "error": "Неверные данные платежа"
    }
