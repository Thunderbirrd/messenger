from PyQt5.QtWidgets import QDialog, QPushButton, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt


# Класс окна со статистикой пользователей
class StatWindow(QDialog):
    '''
    Класс - окно со статистикой пользователей
    '''
    def __init__(self, database):
        super().__init__()

        self.database = database
        self.init_ui()

    def init_ui(self):
        # Настройки окна:
        self.setWindowTitle('Статистика клиентов')
        self.setFixedSize(600, 700)
        self.setAttribute(Qt.WA_DeleteOnClose)

        # Кнапка закрытия окна
        self.close_button = QPushButton('Закрыть', self)
        self.close_button.move(250, 650)
        self.close_button.clicked.connect(self.close)

        # Лист с собственно статистикой
        self.stat_table = QTableView(self)
        self.stat_table.move(10, 10)
        self.stat_table.setFixedSize(580, 620)

        self.create_stat_model()

    # Функция реализующая заполнение таблицы историей сообщений.
    def create_stat_model(self):
        '''Метод реализующий заполнение таблицы статистикой сообщений.'''
        # Список записей из базы
        stat_list = self.database.message_history()

        # Объект модели данных:
        list_model = QStandardItemModel()
        list_model.setHorizontalHeaderLabels(
            ['Имя Клиента', 'Последний раз входил', 'Сообщений отправлено', 'Сообщений получено'])
        for row in stat_list:
            user, last_seen, sent, recvd = row
            user = QStandardItem(user)
            user.setEditable(False)
            last_seen = QStandardItem(str(last_seen.replace(microsecond=0)))
            last_seen.setEditable(False)
            sent = QStandardItem(str(sent))
            sent.setEditable(False)
            recvd = QStandardItem(str(recvd))
            recvd.setEditable(False)
            list_model.appendRow([user, last_seen, sent, recvd])
        self.stat_table.setModel(list_model)
        self.stat_table.resizeColumnsToContents()
        self.stat_table.resizeRowsToContents()
