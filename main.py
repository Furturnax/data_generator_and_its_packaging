import pandas as pd
from mimesis import Generic
from mimesis.locales import Locale



# class ImportData:
#     """
#     Печатает диалоговое онко и предлагает
#     импортировать или создать файл с данными.
#     """

#     def chois():
#         print('Привет. Я программа способная создать архив с '
#               'твоими данными :3\n'
#               'Давай выберем, что необходимо заархивировать\n'
#               '1. Загрузить файл с компьютера.\n'
#               '2. Записать данные самостоятельно.\n'
#               '3. Сгенерировать данные.')

#         while True:
#             try:
#                 user_choise = int(input('Напиши цифру нужного действия: '))
#             except ValueError:
#                 print('Нужна цифра.')

#             if user_choise == 1:
#                 print('Пока в разработке')
#                 break
#             elif user_choise == 2:
#                 print('Пока в разработке')
#                 break
#             elif user_choise == 3:
#                 print('Пока в разработке')
# value_num_rows: int = int(input('Введите желаемое количество строк: '))
#                 break
#             else:
#                 print('Извини, но действие не выполнено, давай ещё раз.')

def write_num_rows() -> int:
    """Проверка введенного значения на корректность."""
    value_num_rows: int = int(input('Введите желаемое количество строк: '))
    if value_num_rows <= 2_000_000:
        return value_num_rows
    raise ValueError(
        'Количество строк больше 2 000 000. Экспорт не выполнится.'
        )


NUM_ROWS: int = write_num_rows()
NAME_FILE: str = 'DataFrame'
NAME_COLUMNS: list[str] = ['Имя', 'Адресс', 'Почтовый индекс',
                           'День Рождения', 'Паспорт',
                           'Номер телефона', 'E-mail',
                           'Работа', 'Банковская карта',
                           'Операционная система телефона']


class GeneratorData:
    """Генерация синтетических данныхс использованием библиотеки mimesis."""

    NAME_COLUMNS: list[str] = ['Имя', 'Адресс', 'Почтовый индекс',
                               'День Рождения', 'Паспорт',
                               'Номер телефона', 'E-mail',
                               'Работа', 'Банковская карта',
                               'Операционная система телефона']

    def __init__(self, NUM_ROWS) -> None:
        self.num: int = NUM_ROWS
        self.generic: Generic = Generic(locale=Locale.RU)

    def generate_data(self) -> list:
        """
        Создает, записывает и возвращает
        таблицу сгенерированных данных.
        """
        uniq_data: list = []
        for _ in range(NUM_ROWS):
            full_name = self.generic.person.full_name()
            address = self.generic.address.address()
            post_code = self.generic.address.postal_code()
            date_of_birth = self.generic.datetime.date().strftime('%Y-%m-%d')
            passport = self.generic.random.randint(1000000000, 9999999999)
            number = self.generic.person.phone_number()
            email = self.generic.person.email()
            job = self.generic.person.occupation()
            card_number = self.generic.payment.credit_card_number()
            os = self.generic.random.choice(['iOS', 'Android'])
            uniq_data.append([full_name, address, post_code, date_of_birth,
                              passport, number, email, job, card_number, os])
        return uniq_data

    def generate_dataframe(self):
        """Генерирует таблицу данных."""
        data: list = GeneratorData(NUM_ROWS).generate_data()
        dataframe = pd.DataFrame(data, columns=NAME_COLUMNS)
        return dataframe


class ExportData(GeneratorData):
    """Экспорт данных в файл."""

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def export_to_excel(self, filename=None):
        """Экспорт сгенерированной таблицы данных в файл Excel."""
        if NUM_ROWS <= 1_000_000:
            self.dataframe.to_excel(filename, index=False, engine='openpyxl')
            print('Данные экспортированы в XLSX файл.')
        elif 1_000_000 < NUM_ROWS <= 2_000_000:
            self.dataframe_part_1 = self.dataframe.iloc[:1_000_000]
            self.dataframe_part_2 = self.dataframe.iloc[1_000_000:2_000_000]
            self.dataframe_part_1.to_excel(f'{NAME_FILE}_часть_1.xlsx',
                                           index=False, engine='openpyxl')
            self.dataframe_part_2.to_excel(f'{NAME_FILE}_часть_2.xlsx',
                                           index=False, engine='openpyxl')
            print('Данные экспортированы в два XLSX '
                  'файла с именами '
                  f'{NAME_FILE}_часть_1 и '
                  f'{NAME_FILE}_часть_2')

    def export_to_csv(self, filename):
        """Экспорт сгенерированной таблицы данных в файл Csv."""
        self.dataframe.to_csv(filename, index=False)
        print('Данные экспортированы в CSV файл.')

    def export_to_txt(self, filename):
        """Экспорт сгенерированной таблицы данных в файл Txt."""
        self.dataframe.to_csv(filename, index=False, sep='\t')
        print('Данные экспортированы в TXT файл.')


class ZipData:
    pass


data_exporter = ExportData(GeneratorData.generate_dataframe(NUM_ROWS))
data_exporter.export_to_csv(f'{NAME_FILE}.csv')
data_exporter.export_to_txt(f'{NAME_FILE}.txt')
data_exporter.export_to_excel(f'{NAME_FILE}.xlsx')


# if __name__ == "__main__":
    # ImportData.chois()
    # data_exporter = ExportData(GeneratorData.generate_dataframe(50))
    # print(GeneratorData.generate_dataframe(50))
    # data_exporter.export_to_csv(f'{}.csv')
    # data_exporter.export_to_txt(f'{}.txt')
    # data_exporter.export_to_excel(f'{}.xlsx')



    # def write_num_rows() -> int:
    #     """Проверка введенного значения строк на корректность."""
    #     while True:
    #         try:
    #             value_num_rows: int = int(input('Введите желаемое'
    #                                             'количество строк: '))
    #         except ValueError:
    #             print('Нужно значение в виде цифры.')

    #         if value_num_rows <= 2_000_000:
    #             return value_num_rows
    #         raise ValueError(
    #             'Количество строк больше 2 000 000. Экспорт не выполнится.'
    #             )
