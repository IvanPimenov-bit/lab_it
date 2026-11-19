from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QInputDialog
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)
        self.init_ui()
        self.connect_signals()
    def init_ui(self):
        central=QWidget()
        self.setCentralWidget(central)
        main_layout=QVBoxLayout()
        central.setLayout(main_layout)
        self.title_label=QLabel("Новая задача")
        self.task_input=QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button=QPushButton("Добавить")
        self.task_list=QListWidget()
        self.delete_button=QPushButton("Удалить")
        self.clear_button=QPushButton("Очистить всё")
        self.done_button=QPushButton("Выполнено")
        self.counter_label=QLabel("Количество задач: 0")
        input_row=QHBoxLayout()
        input_row.addWidget(self.task_input)
        input_row.addWidget(self.add_button)
        buttons_row=QHBoxLayout()
        buttons_row.addWidget(self.delete_button)
        buttons_row.addWidget(self.clear_button)
        buttons_row.addWidget(self.done_button)
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(input_row)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(buttons_row)
        main_layout.addWidget(self.counter_label)
    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_tasks)
        self.task_input.returnPressed.connect(self.add_task)
        self.done_button.clicked.connect(self.mark_done)
    def add_task(self):
        text=self.task_input.text().strip()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
            return
        self.task_list.addItem(text)
        self.task_input.clear()
        self.update_counter()
        self.statusBar().showMessage("Задача добавлена")
    def delete_task(self):
        row=self.task_list.currentRow()
        if row<0:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления")
            return
        answer=QMessageBox.question(self, "Удаление", "Удалить выбранную задачу?")
        if answer==QMessageBox.StandardButton.Yes:
            self.task_list.takeItem(row)
            self.update_counter()
            self.statusBar().showMessage("Задача удалена")
    def clear_tasks(self):
        if self.task_list.count()==0:
            return  
        answer=QMessageBox.question(self, "Очистка", "Удалить все задачи?")
        if answer==QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()
            self.statusBar().showMessage("Список очищен")
    def mark_done(self):
        item = self.task_list.currentItem()
        if item is None:
            return
        if not item.text().startswith("✓ "):
            item.setText("✓ " + item.text())
        self.update_counter()
    def update_counter(self):
        count=self.task_list.count()
        done=sum(1 for i in range(count)
                   if self.task_list.item(i).text().startswith("✓ "))
        self.counter_label.setText(f"Количество задач: {count} (выполнено: {done})")
        self.setWindowTitle(f"Менеджер задач ({count})")
   