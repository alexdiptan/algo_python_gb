# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.

import collections


def generate_company_data(count_companies):
    """
    :param count_companies: Кол-во компаний
    :return: {"name": "company_name", "average_profit_for_quarter": [list]}
    """
    data_list = collections.defaultdict(list)

    for company_name in range(count_companies):
        comp_name = input('Введите название компании: ')
        _ = [data_list[comp_name].append(0) for _ in range(4)]  # инициализирую список и заполняю его нулями
        for ind, quarter_profit in enumerate(range(len(data_list[comp_name]))):
                data_list[comp_name][ind] = float(input(f'Введите доход 'f'за {quarter_profit+1} квартал: '))

    return data_list


def average_profit(company_data):
    return sum(company_data) / len(company_data)


def get_average_profit_by_company(company_dict):
    """
    :param company_dict: Словарь вида {"name": "company_name", "average_profit_for_quarter": [list]}
    :return: Словарь вида {"name": "company_name", "average_profit_for_year": [list]}
    """
    average_profit_by_company_for_year = {}

    for company_name, income in company_dict.items():
        average_profit_by_company_for_year[company_name] = average_profit(income)

    return average_profit_by_company_for_year


if __name__ == '__main__':
    camp_comp = get_average_profit_by_company(generate_company_data(4))

    average_company_income = [income for income in camp_comp.values()]
    av_prof = average_profit(average_company_income)
    print(f'Средний доход всех компаний за год: {av_prof}.')
    print(f'Компании, чей доход за год выше среднего по всем компаниям:')
    for company_name, average_company_income_for_year in camp_comp.items():
        if average_company_income_for_year > av_prof:
            print(f' - {company_name} - {average_company_income_for_year}')

    print(f'Компании, чей доход за год ниже среднего по всем компаниям:')
    for company_name, average_company_income_for_year in camp_comp.items():
        print(f' - {company_name} - {average_company_income_for_year}')


"""
Введите название компании: epam
Введите доход за 1 квартал: 31235
Введите доход за 2 квартал: 44232
Введите доход за 3 квартал: 34245
Введите доход за 4 квартал: 53244
Введите название компании: DataArt
Введите доход за 1 квартал: 223324
Введите доход за 2 квартал: 323132
Введите доход за 3 квартал: 31211
Введите доход за 4 квартал: 133453
Введите название компании: Google
Введите доход за 1 квартал: 321332313
Введите доход за 2 квартал: 32132
Введите доход за 3 квартал: 12321313
Введите доход за 4 квартал: 12321467
Введите название компании: VK
Введите доход за 1 квартал: 786854
Введите доход за 2 квартал: 46455
Введите доход за 3 квартал: 64564
Введите доход за 4 квартал: 645645
Средний доход всех компаний за год: 21776551.1875.
Компании, чей доход выше среднего по всем компаниям:
 - Google - 86501806.25
Компании, чей доход ниже среднего по всем компаниям:
 - epam - 40739.0
 - DataArt - 177780.0
 - Google - 86501806.25
 - VK - 385879.5
"""