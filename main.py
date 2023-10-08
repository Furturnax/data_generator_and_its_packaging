import pandas as pd
from mimesis import Generic
from mimesis.locales import Locale
import zipfile
from py7zr import SevenZipFile


class GeneratorData:
    """Генерация синтетических данныхс использованием библиотеки mimesis."""

    def __init__(self) -> None:
        self.generic: Generic = Generic(locale=Locale.RU)

    def write_num_rows(self, input_number) -> int:
        """Проверка введенного значения на корректность."""
        if input_number <= 2_000_000:
            return input_number
        raise ValueError(
            'Количество строк больше 2 000 000. Экспорт не выполнится.'
            )

    def generate_data(self) -> list:
        """
        Создает, записывает и возвращает
        таблицу сгенерированных данных.
        """
        uniq_data: list = []
        for _ in range(user_input):
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
        data: list = self.generate_data()
        name_columns: list[str] = ['Имя', 'Адресс', 'Почтовый индекс',
                                   'День Рождения', 'Паспорт',
                                   'Номер телефона', 'E-mail',
                                   'Работа', 'Банковская карта',
                                   'Операционная система телефона']
        dataframe = pd.DataFrame(data, columns=name_columns)
        return dataframe


class ExportData(GeneratorData):
    """Экспорт данных в файл."""

    def __init__(self, dataframe, user_input):
        self.dataframe = dataframe
        self.user_input: int = user_input

    def export_to_excel(self, filename=None):
        """Экспорт сгенерированной таблицы данных в файл Excel."""
        if user_input <= 1_000_000:
            self.dataframe.to_excel(filename, index=False, engine='openpyxl')
            print('Данные экспортированы в XLSX файл.')
        elif 1_000_000 < user_input <= 2_000_000:
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
    """Архивация данных в файл."""

    def create_zip(output_filename, *files_to_archive):
        with zipfile.ZipFile(output_filename, 'w',
                             zipfile.ZIP_DEFLATED) as zip:
            for file_to_archive in files_to_archive:
                zip.write(file_to_archive)

    def create_7z(output_filename, *files_to_archive):
        with SevenZipFile(output_filename, 'w') as sz:
            for file_to_archive in files_to_archive:
                sz.write(file_to_archive)


def menu():
    print('\nПривет. Я программа способная создать архив с '
          'твоими данными :3\n'
          'Давай выберем, нужное действие:\n'
          '\n1. Загрузить файл с компьютера.\n'
          '2. Записать данные самостоятельно.\n'
          '3. Сгенерировать данные.\n')


def file_format_choise():
    print('\nВ каком кормате хотите сохранить данные?\n'
          '1. В формате Excel.\n'
          '2. В формате CSV\n'
          '3. В формате TXT\n'
          '4. Все форматы сразу\n')

    while True:
        try:
            file_format: int = int(input('Выберети номер действия: '))
        except ValueError:
            print('Нужна цифра.')

        if file_format == 1:
            data_exporter.export_to_excel(f'{NAME_FILE}.xlsx')
            zipping('xlsx')
            break
        elif file_format == 2:
            data_exporter.export_to_csv(f'{NAME_FILE}.csv')
            zipping('csv')
            break
        elif file_format == 3:
            data_exporter.export_to_txt(f'{NAME_FILE}.txt')
            zipping('txt')
            break
        elif file_format == 4:
            data_exporter.export_to_excel(f'{NAME_FILE}.xlsx')
            data_exporter.export_to_csv(f'{NAME_FILE}.csv')
            data_exporter.export_to_txt(f'{NAME_FILE}.txt')
            zipping('all')
            break
        else:
            print('Извини, но действие не выполнено, давай ещё раз.')


def zipping(*formats):
    print('\nАрхивируем данные?\n'
          '1. Да.\n'
          '2. Нет.\n')
    while True:
        try:
            choise_archive: int = int(input('Выберети номер действия: '))
        except ValueError:
            print('Нужна цифра.')

        if choise_archive == 1:
            NAME_ZIP: str = str(input('Введите имя архива: '))
            print('\nВыберите формат архивации:\n'
                  '1. Zip.\n'
                  '2. 7z.\n')
            while True:
                try:
                    type_zip: int = int(input('Выберети номер действия: '))
                except ValueError:
                    print('Нужна цифра.')

                while True:
                    if type_zip == 1:
                        for format in formats:
                            if format == 'xlsx':
                                ZipData.create_zip(f'{NAME_ZIP}.zip',
                                                   f'{NAME_FILE}.xlsx')
                            elif format == 'csv':
                                ZipData.create_zip(f'{NAME_ZIP}.zip',
                                                   f'{NAME_FILE}.csv')
                            elif format == 'txt':
                                ZipData.create_zip(f'{NAME_ZIP}.zip',
                                                   f'{NAME_FILE}.txt')
                            elif format == 'all':
                                ZipData.create_zip(f'{NAME_ZIP}.zip',
                                                   f'{NAME_FILE}.xlsx',
                                                   f'{NAME_FILE}.csv',
                                                   f'{NAME_FILE}.txt')
                            else:
                                print('Ошибка, таких форматов нет.')
                        print('Архив создан.')
                        print('Спасибо, что воспользовались моей программой.')
                        break
                    elif type_zip == 2:
                        for format in formats:
                            if format == 'xlsx':
                                ZipData.create_7z(f'{NAME_ZIP}.7z',
                                                  f'{NAME_FILE}.xlsx')
                            elif format == 'csv':
                                data_exporter.export_to_csv(f'{NAME_FILE}.csv')
                                ZipData.create_7z(f'{NAME_ZIP}.7z',
                                                  f'{NAME_FILE}.csv')
                            elif format == 'txt':
                                ZipData.create_7z(f'{NAME_ZIP}.7z',
                                                  f'{NAME_FILE}.txt')
                            elif format == 'all':
                                ZipData.create_7z(f'{NAME_ZIP}.7z',
                                                  f'{NAME_FILE}.xlsx',
                                                  f'{NAME_FILE}.csv',
                                                  f'{NAME_FILE}.txt')
                            else:
                                print('Ошибка, таких форматов нет')
                        print('Архив создан.')
                        print('Спасибо, что воспользовались моей программой.')
                        break
                    else:
                        print('Такого действия нет.')

        elif choise_archive == 2:
            data_exporter.export_to_excel(f'{NAME_FILE}.xlsx')
            data_exporter.export_to_csv(f'{NAME_FILE}.csv')
            data_exporter.export_to_txt(f'{NAME_FILE}.txt')
            print('Спасибо, что воспользовались моей программой.')
            break
        else:
            print('Такого действия нет.')


if __name__ == "__main__":
    menu()
    while True:
        try:
            user_choise: int = int(input('Напиши цифру нужного действия: '))
        except ValueError:
            print('Нужна цифра.')

        if user_choise == 1:
            print('Пока в разработке.')
            break
        elif user_choise == 2:
            print('Пока в разработке.')
            break
        elif user_choise == 3:
            user_input: int = int(input('Введите желаемое количество строк: '))
            GeneratorData().input_number = GeneratorData().write_num_rows(
                user_input
                )
            data_exporter = ExportData(
                GeneratorData().generate_dataframe(), user_input
                )
            NAME_FILE = str(input('Как назовём файл? '))
            file_format_choise()
        else:
            print('Извини, но действие не выполнено, давай ещё раз.')
