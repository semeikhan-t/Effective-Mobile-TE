#TODO
# Реализовать телефонный справочник со следующими возможностями:
# 1. Вывод постранично записей из справочника на экран
# 2. Добавление новой записи в справочник
# 3. Возможность редактирования записей в справочнике
# 4. Поиск записей по одной или нескольким характеристикам
# Требования к программе:
# 1. Реализация интерфейса через консоль (без веб- или графического интерфейса)
# 2. Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
# 3. В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)
# Плюсом будет:
# 1. аннотирование функций и переменных
# 2. документирование функций
# 3. подробно описанный функционал программы
# 4. размещение готовой программы и примера файла с данными на github

from traceback import print_exc
from time import sleep


def func_1_view():
    """
    Функция для постраничного просмотра всех записей в справочнике.
    Открывает файл 'contacts.txt' и выводит записи постранично.
    """
    PAGE_SIZE = 5  # количество записей на одной странице

    with open('contacts.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pages = [lines[i:i + PAGE_SIZE] for i in range(0, len(lines), PAGE_SIZE)]  # разделение записей на страницы

    page_number = 0
    while True:
        print(f'Страница {page_number + 1} из {len(pages)}:')
        for line in pages[page_number]:
            print(line.strip())

        user_input = input('Введите "n" для следующей страницы, "p" для предыдущей страницы или "q" для выхода: ')
        print('\n')
        if user_input == 'n' and page_number < len(pages) - 1:
            page_number += 1
        elif user_input == 'p' and page_number > 0:
            page_number -= 1
        elif user_input == 'q':
            break
        else:
            print('Неверный ввод, попробуйте еще раз.')


def func_2_add():
    """
        Функция для добавления новой записи в справочник.
        Запрашивает у пользователя данные для новой записи,
        затем добавляет эту запись в файл 'contacts.txt'.
    """
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    organization = input('Введите название организации: ')
    work_phone = input('Введите рабочий телефон: ')
    personal_phone = input('Введите личный телефон: ')
    with open('contacts.txt', 'a', encoding='utf-8') as file:  # Открытие и запись полученных данных в файл справочник
        file.write(f'{surname}, {name}, {patronymic}, {organization}, {work_phone}, {personal_phone}\n')


def func_3_edit():
    """
        Функция для редактирования записи в справочнике.
        Запрашивает у пользователя фамилию для редактирования,
        затем находит соответствующую запись в файле 'contacts.txt' и изменяет ее.
    """
    surname = input('Введите фамилию для редактирования: ')
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('contacts.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            if line.startswith(surname):
                print('Текущая запись: ', line)
                surname = input('Введите новую фамилию: ')
                name = input('Введите новое имя: ')
                patronymic = input('Введите новое отчество: ')
                organization = input('Введите новое название организации: ')
                work_phone = input('Введите новый рабочий телефон: ')
                personal_phone = input('Введите новый личный телефон: ')
                line = f'{surname}, {name}, {patronymic}, {organization}, {work_phone}, {personal_phone}\n'
            file.write(line)


def func_4_search():
    """
    Функция для поиска записей в справочнике.
    Запрашивает у пользователя данные для поиска,
    затем находит и выводит все записи, содержащие эти данные.
    """
    search = input('Введите данные для поиска: ')
    found = False  # флаг для отслеживания найденных совпадений
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if search in line:
                print(line.strip())
                found = True  # если найдено совпадение, устанавливаем флаг в True
    if not found:  # если после цикла флаг остался False, выводим сообщение
        print('По запросу %s ничего не найдено :(' % search)



def run_menu():
    menu_str = '''
        [1] Вывод записей из справочника на экран
        [2] Добавить новую запись в справочник
        [3] Редактировать запись в справочнике
        [4] Поиск записи
        [0] Выйти
    '''

    while True:
        print(menu_str)

        user_input = input('>>> ')  # Ввод команды пользователем

        if user_input == '0':  # Обработка команды "Выйти", прекращение работы
            print('Bye bye :)')
            break

        try:                        # Запуск команды запрашиваемой пользователем
            if user_input == '1':
                func_1_view()
            elif user_input == '2':
                func_2_add()
            elif user_input == '3':
                func_3_edit()
            elif user_input == '4':
                func_4_search()
            else:  # Предупреждение о том что введенная пользователем команда не существует
                print('Такой команды не существует!')
                continue

        except Exception:  # Обработка ошибок
            print('Ошибка действия %s!' % user_input)
            print_exc()
            sleep(3)
            input('Нажмите Enter для продолжения...')
            continue


if __name__ == '__main__':
    run_menu()
