#Gregory Pereverzev 22.11.2019
#Программа показывающая устройство хранения словаря в словаре с последующим обращением к данным.
#Импортируем функцию для "красивого" вывода словарей на экран.
import pprint

#Создаем пустой словарь, далее сохраняем с каждым ключем "вложенные" словари.
people = {}
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home planet': 'Betelgeuse seven'}
people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupayion': 'Sandwich-Maker',
                    'Home planet': 'Earth'}
people['Trillian'] = {'Name': 'Tricia McMillan',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home planet': 'Earth'}
people['Robot'] = {'Name': 'Marvin',
                   'Gender': 'Unknown',
                   'Occupation': 'Paranoid Android',
                   'Home planet': 'Unknown'}
#"Красиво" выводим содержание словаря на экран.
pprint.pprint(people)
#Получаем значение из "вложенного" чсловаря.
print(people['Ford'] ['Occupation'])