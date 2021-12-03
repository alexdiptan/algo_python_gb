# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

final_symbols = ''
i = 1

for symbol in range(32, 128):
    final_symbols += f'{symbol}-{chr(symbol)}    '
    if i % 10 == 0:
        final_symbols += '\n'
    i += 1

print(final_symbols)

