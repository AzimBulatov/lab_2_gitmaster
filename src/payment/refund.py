"""
Модуль для возврата платежей
"""

def refund_payment(transaction_id, amount):
    """
    Функция для возврата платежа
    
    Args:
        transaction_id (str): ID транзакции
        amount (float): Сумма возврата
        
    Returns:
        dict: Результат возврата
    """
    if transaction_id and amount > 0:
        print(f"Возврат {amount} по транзакции {transaction_id} выполнен")
        return {
            "status": "refunded",
            "amount": amount,
            "refund_id": "REF789012"
        }
    return {
        "status": "failed",
        "error": "Неверные данные для возврата"
    }
