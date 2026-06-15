
import math

def calculate_work_days(month_days, work_days, rest_days):
    """
    Универсальная формула расчета рабочих и выходных дней в месяце.
    
    Параметры:
    - month_days: количество дней в месяце (28-31)
    - work_days: количество рабочих дней в цикле (первое число графика)
    - rest_days: количество выходных дней в цикле (второе число графика)
    
    Возвращает:
    - total_work: общее количество рабочих дней
    - total_rest: общее количество выходных дней
    - full_cycles: количество полных циклов
    - remaining_days: оставшиеся дни в конце месяца
    """
    
    cycle_length = work_days + rest_days  # длина одного цикла
    
    # Количество полных циклов в месяце
    full_cycles = month_days // cycle_length
    
    # Оставшиеся дни после полных циклов
    remaining_days = month_days % cycle_length
    
    # Рабочие дни из полных циклов
    work_from_full = full_cycles * work_days
    
    # Выходные дни из полных циклов
    rest_from_full = full_cycles * rest_days
    
    # Оставшиеся дни: если их меньше или равно work_days, все они рабочие
    # Если больше, то work_days рабочих и остальные выходные
    if remaining_days <= work_days:
        work_remaining = remaining_days
        rest_remaining = 0
    else:
        work_remaining = work_days
        rest_remaining = remaining_days - work_days
    
    # Итого
    total_work = work_from_full + work_remaining
    total_rest = rest_from_full + rest_remaining
    
    return {
        'total_work': total_work,
        'total_rest': total_rest,
        'full_cycles': full_cycles,
        'remaining_days': remaining_days,
        'work_remaining': work_remaining,
        'rest_remaining': rest_remaining
    }

# Проверим на примерах
schedules = [(5, 2), (4, 3), (4, 4), (4, 2), (3, 3), (3, 2), (2, 3)]
months = [28, 29, 30, 31]

print("=" * 80)
print("УНИВЕРСАЛЬНАЯ ФОРМУЛА РАСЧЕТА РАБОЧИХ/ВЫХОДНЫХ ДНЕЙ В МЕСЯЦЕ")
print("=" * 80)
print()

for schedule in schedules:
    w, r = schedule
    cycle = w + r
    print(f"\n{'─' * 70}")
    print(f"График {w}/{r} (цикл: {cycle} дней)")
    print(f"{'─' * 70}")
    print(f"{'Месяц':<8} {'Дней':<6} {'Циклов':<8} {'Остаток':<8} {'Рабочих':<10} {'Выходных':<10}")
    print(f"{'-' * 70}")
    
    for md in months:
        result = calculate_work_days(md, w, r)
        print(f"{md:>3} дней  {md:<6} {result['full_cycles']:<8} {result['remaining_days']:<8} "
              f"{result['total_work']:<10} {result['total_rest']:<10}")

print("\n" + "=" * 80)