def mask_account_card(info):
    """Для маскировки номера карты/счета"""
    # Разделяем строку на тип и номер
    parts = info.split()
    card_type = parts[0]
    number = parts[1]
    # Проверяем тип и применяем соответствующую маскировку
    if card_type in ["Visa", "MasterCard", "Maestro", "AmericanExpress"]:
        return f"{card_type} {mask_card_number(number)}"
    elif card_type == "Счет":
        return f"{card_type} {mask_account_number(number)}"
    else:
        raise ValueError("Неизвестный тип карты или счета")

    def get_date(date_str):
        """Функция форматирования даты"""
        # Разделяем строку по символу 'T'
        date_part = date_str.split("T")[0]
        # Разделяем дату на компоненты (год, месяц, день) и форматируем
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
