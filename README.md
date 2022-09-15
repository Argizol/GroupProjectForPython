# :phone: Телефонный справочник :registered:
## :bookmark_tabs: ТЗ:
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.  
Под форматами понимаем структуру файлов, например: в файле на одной строке хранится одна часть записи, пустая строка - разделитель.
## :alarm_clock: Дедлайн: 
22.09.2022, но планируем закончить раньше
## :man_technologist: Команда: 
- [Дмитрий](https://github.com/Argizol):  тимлид, основные команды
- [Виктор](https://github.com/TheLi4e):  UI, Логирование
- [Ксения](https://github.com/letusbeus):  Импорт/Экспорт, README.md
- [Роман](https://github.com/AndarkRA):  Сведение всех классов в итоговый проект
## :hammer_and_wrench: Структура  
### 
- main.py - основной модуль проекта, запуск приложения  
- UI.py - view  
- ExitCommand.py - завершение работы приложения  
### Логирование
- error.csv - реестр ошибок  
- log.csv - реестр изменений объектов приложения  
- logger.py - логгер проекта  
### Работа с файлами
- ImportFile.py - импорт файла телефонного справочника    
- ExportFile.py - экспорт файла телефонного справочника    
- phonebook.csv - файл импортируемого телефонного справочника  
- exported_phonebook.csv - файл экспортируемого телефонного справочника (создается при выборе опции экспорта при завершении работы приложения)  
- Contacts.py - временное хранилище импортируемого телефонного справочника, используемое при работе приложения  
### DAO (Data Access Object)  
- AddCommand.py - добавление контакта  
- DeleteCommand.py - удаление контакта  
- EditCommand.py - редактирование контакта  
- ReadCommand.py - чтение справочника  
- FindCommands.py - поиск контакта   
## :floppy_disk: Что необходимо для запуска проекта  
#### Запуск через терминал   
- Открыть терминал  
- Перейти в папку проекта phonebook  
- Для запуска приложения ввести 'python PhoneBookPython/main.py' без кавычек  
- Следовать инструкциям, выводимым в консоль  
#### Запуск в среде разработки  
- Открыть проект phonebook  
- Запустить файл main.py  
- Следовать инструкциям, выводимым в консоль 
## :white_check_mark: Сделано:  
До 18:00 12.09.2022:  
:heavy_check_mark:Выбрать задачу  
:heavy_check_mark:Сформировать команду  
:heavy_check_mark:Определить руководителя на проекте  
:heavy_check_mark:Создать репозиторий(скорее всего ответственность руководителя), добавив Readme с указанием необходимой информации (задача, команда, дедлайн, модули т. д.  
:heavy_check_mark:Распределить роли и зоны ответственности между участниками  
:heavy_check_mark:Приступить к реализации проекта (каждому ответственному за модуль описать в файле соответствующего модуля, какие методы он планирует применять для реализации  
:heavy_check_mark:Обсудить каждый модуль командой и приступить к написанию кода  
До 18:00 15.09.2022:  
:heavy_check_mark:Реализовать импорт словаря (создание пустого словаря в случае отказа от импорта)  
:heavy_check_mark:Реализовать сохранение словаря в файл  
:heavy_check_mark:Реализовать чтение всего словаря  
:heavy_check_mark:Реализовать поиск контакта по имени или номеру абонента, выбор контакта из результатов поиска  
:heavy_check_mark:Реализовать добавление нового абонента в словарь  
До 18:00 19.09.2022:  
:heavy_check_mark:Реализовать логгирование изменений при работе со словарем  
:heavy_check_mark:Реализовать удаление контакта по имени или номеру абонента  
:heavy_check_mark:Реализовать редактирование имени абонента и/или номера  
:heavy_check_mark:Реализовать логгирование ошибок, возникающих при работе со словарем  
До 18:00 22.09.2022:  
:x:Интегрировать телеграмм-бота  
:x:Отрефакторить существующий код  
:x:Релиз :tada:  
