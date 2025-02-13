import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTimeEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtMultimedia import QSound


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("my_timer_app")
        self.setGeometry(0, 0, 350, 250)
        self.setFixedSize(350, 250)
        self.setWindowIcon(QIcon('title_pic.jpg'))
        self.setStyleSheet('background-color: rgb(234, 160, 153);')

        # center widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # sounds
        self.button_sound = QSound('click_2.wav')
        self.break_sound = QSound('break_sound.wav')
        self.end_timer_sound = QSound('end2_sound.wav')

        # go button
        self.goButton = QPushButton('go', self.centralwidget)
        self.goButton.setGeometry(140, 130, 61, 51)
        self.goButton.setStyleSheet(
            "border-color: rgb(252, 231, 231);"
            "color: rgb(252, 231, 231);"
            "font: 75 20pt \"Unispace\";"
            "background: #AA7D7D;"
            )

        # main label
        self.header = QLabel(' < timer >', self.centralwidget)
        self.header.setFont(QFont('Unispace', 28))
        self.header.setGeometry(50, 40, 251, 81)
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setStyleSheet(
            "color: rgb(170, 125, 125);"
            "font: 75 28pt \"Unispace\";"
            "background: #F4C9C9;")

        # reset button
        self.resetButton = QPushButton('reset', self.centralwidget)
        self.resetButton.setFont(QFont('Unispace', 18))
        self.resetButton.setGeometry(30, 190, 81, 41)
        self.resetButton.setStyleSheet(
            'border-color: rgb(252, 231, 231);'
            'color: rgb(252, 231, 231);'
            'font: 75 18pt \"Unispace\";'
            'background: #AA7D7D;'
        )

        self.resetButton.hide()

        # start button
        self.startButton = QPushButton('start', self)
        self.startButton.setFont(QFont('Unispace', 18))
        self.startButton.setGeometry(130, 190, 81, 41)
        self.startButton.setStyleSheet(
            'border-color: rgb(252, 231, 231);'
            'color: rgb(252, 231, 231);'
            'font: 75 18pt \"Unispace\";'
            'background: #AA7D7D;'
        )
        self.startButton.hide()

        # stop button
        self.stopButton = QPushButton('stop', self.centralwidget)
        self.stopButton.setFont(QFont('Unispace', 18))
        self.stopButton.setGeometry(230, 190, 81, 41)
        self.stopButton.setStyleSheet(
            'border-color: rgb(252, 231, 231);'
            'color: rgb(252, 231, 231);'
            'font: 75 18pt \"Unispace\";'
            'background: #AA7D7D;'
        )
        self.stopButton.hide()

        # set_timer button >  return to start after finished time
        self.set_timer = QPushButton("set_timer", self.centralwidget)
        self.set_timer.setGeometry(100, 180, 141, 51)
        self.set_timer.setStyleSheet(
            "border-color: rgb(252, 231, 231);"
            "color: rgb(252, 231, 231);"
            "font: 75 16pt \"Unispace\";"
            "position: absolute;"
            "background: #AA7D7D;"
        )
        self.set_timer.hide()

        # vertical frame for end window
        self.verticalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_2.setGeometry(110, 90, 121, 81)
        self.verticalFrame_2.setStyleSheet(
            "background - color: rgb (252, 231, 231);"
        )
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame_2)

        self.gif_label = QLabel(self.verticalFrame_2)
        self.gif_label.setGeometry(0,0, self.verticalFrame_2.width(), self.verticalFrame_2.height())

        self.gif_movie = QtGui.QMovie("gifend_2.gif")
        self.gif_label.setMovie(self.gif_movie)

        self.verticalFrame_2.hide()

        # vertical frame for break window
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(29, 49, 291, 161)
        self.verticalFrame.setStyleSheet(
            "background-color: rgb(244, 201, 201);"
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.text = QLabel('>>> drink some water\n>>> stretch your legs\n>>> give your eyes a rest',
                           self.verticalFrame)
        self.text.setStyleSheet(
            "font: 75 13pt \"Unispace\";"
            "color: rgb(170, 125, 125);"
        )
        self.verticalLayout.addWidget(self.text)
        self.verticalFrame.hide()

        # timer_edit
        self.time_edit = QTimeEdit(self.centralwidget)
        self.time_edit.setTime(QTime(0, 0, 0))
        self.time_edit.setDisplayFormat('hh-mm-ss')
        self.time_edit.setGeometry(50, 110, 261, 61)
        self.time_edit.setStyleSheet(
            'font: 75 32pt \"Unispace\";'
            'background-color: rgb(248, 212, 212);'
            'font-weight: 400;'
            'color: rgb(132, 97, 97);'
            'border: 1px solid #FCE7E7;'
        )
        self.time_edit.hide()

        # break time edit
        self.break_time_edit = QTimeEdit(self.centralwidget)
        self.break_time_edit.setTime(QTime(0, 0, 0))
        self.break_time_edit.setDisplayFormat('mm:ss')
        self.break_time_edit.setGeometry(120, 180, 121, 41)
        self.break_time_edit.setStyleSheet(
            "background-color:  rgb(239, 223, 223);"
            "font: 75 20pt \"Unispace\";"
            "color: rgb(170, 125, 125);"
            "border: 1px solid #FCE7E7;"
        )
        self.break_time_edit.hide()

        #  timer settings
        self.main_timer = QTimer()
        self.remaining_time = QTime(0, 0)

        self.break_timer = QTimer()
        self.break_remaining_time = QTime(0, 0)

        self.main_secs = 0
        self.break_secs = 0

        self.main_period = 25 * 60
        self.break_period = 5 * 60

        self.saved_main_timer = QTime(0, 0)

        self.add_func()

    def add_func(self):
        self.goButton.clicked.connect(self.play_button_sounds)
        self.goButton.clicked.connect(self.timer_window)

        self.resetButton.clicked.connect(self.reset_timer)
        self.resetButton.clicked.connect(self.play_button_sounds)

        self.startButton.clicked.connect(self.play_button_sounds)
        self.startButton.clicked.connect(self.start_timer)

        self.stopButton.clicked.connect(self.stop_timer)
        self.stopButton.clicked.connect(self.play_button_sounds)

        self.set_timer.clicked.connect(self.play_button_sounds)
        self.set_timer.clicked.connect(self.timer_window)

        self.break_timer.timeout.connect(self.update_break_timer)
        self.main_timer.timeout.connect(self.update_main_timer)

    def play_button_sounds(self):
        self.button_sound.play()

    def play_break_sounds(self):
        self.break_sound.play()

    def play_end_sounds(self):
        self.end_timer_sound.play()

    def timer_window(self):
        """Установка таймера"""
        self.set_timer.hide()
        self.header.hide()
        self.goButton.hide()

        self.timer_header = QLabel('< ur_timer >', self.centralwidget)
        self.timer_header.setFont(QFont('Unispace', 28))
        self.timer_header.setGeometry(40, 20, 281, 71)
        self.timer_header.setAlignment(Qt.AlignCenter)
        self.timer_header.setStyleSheet(
            'color: rgb(170, 125, 125);'
            'position: absolute;'
            'background: #F4C9C9;'
            'font: 75 28pt \"Unispace\";'
        )

        self.startButton.show()
        self.stopButton.show()
        self.resetButton.show()
        self.time_edit.show()
        self.timer_header.show()

        self.remaining_time = self.time_edit.time()
        self.time_edit.setEnabled(True)

    def break_window(self):
        self.timer_header.hide()
        self.startButton.hide()
        self.stopButton.hide()
        self.resetButton.hide()
        self.time_edit.hide()

        # new label for break panel
        self.break_header = QLabel('take a break', self.centralwidget)
        self.break_header.setFont(QFont('Unispace', 22))
        self.break_header.setGeometry(60, 20, 231, 51)
        self.break_header.setStyleSheet(
            "font: 75 22pt \"Unispace\";"
            "background-color: rgb(170, 125, 125);"
            "color: rgb(239, 223, 223);"
            )

        self.break_header.show()
        self.break_time_edit.show()
        self.verticalFrame.show()

    def end_window(self):
        self.timer_header.hide()
        self.startButton.hide()
        self.stopButton.hide()
        self.resetButton.hide()
        self.time_edit.hide()

        self.end_header = QLabel("< time's_up >", self.centralwidget)
        self.end_header.setGeometry(40, 20, 271, 61)
        self.end_header.setStyleSheet(
            "color: rgb(170, 125, 125);"
            "font: 75 26pt \"Unispace\";"
            "background: #F4C9C9;"
        )
        self.end_header.show()
        self.set_timer.show()
        self.verticalFrame_2.show()
        self.gif_movie.start()
        self.play_end_sounds()

    def start_timer(self):
        """Начало отсчёта без возможности переустановить время"""
        self.main_secs = 0
        self.remaining_time = self.time_edit.time()
        self.main_timer.start(1000)
        self.time_edit.setEnabled(False)

    def update_main_timer(self):
        """Обновляет таймер каждую секунду в обратном отсчёте,
        по завершению таймера вылезет картинка"""
        self.main_secs += 1
        if self.remaining_time != QTime(0,0):
            self.remaining_time = self.remaining_time.addSecs(-1)
            self.update_time_display()
            if self.main_secs >= self.main_period:
                self.save_current_main_time()
                self.main_timer.stop()
                self.start_break_timer()
                self.play_break_sounds()
        else:
            self.main_timer.stop()
            self.break_timer.stop()
            self.end_window()

    def reset_to_timer(self):
        """Сброс интерфейса к основному таймеру"""
        self.timer_header.show()
        self.startButton.show()
        self.stopButton.show()
        self.resetButton.show()
        self.time_edit.show()

        self.break_header.hide()
        self.verticalFrame.hide()
        self.break_time_edit.hide()

        self.start_timer()

    def start_break_timer(self):
        """Запуск таймера перерыва"""
        self.break_secs = 0
        self.break_remaining_time = QTime(0,0,10)
        self.break_timer.start(1000)
        self.break_time_edit.setEnabled(False)
        self.break_window()

    def update_break_timer(self):
        self.break_secs += 1
        self.break_remaining_time = self.break_remaining_time.addSecs(-1)
        self.update_time_display(is_break_timer=True)

        if self.break_secs >= self.break_period:
            self.break_timer.stop()
            self.reset_to_timer()
            self.start_timer()
            self.play_break_sounds()

    def update_time_display(self, is_break_timer=False):
        """Обновление времени и его сохранении"""
        if is_break_timer:
            self.break_time_edit.setTime(self.break_remaining_time)  # Обновляем время для таймера перерыва
        else:
            self.time_edit.setTime(self.remaining_time)  # Обновляем время для основного таймера

    def save_current_main_time(self):
        self.saved_main_timer = self.remaining_time

    def reset_timer(self):
        self.main_timer.stop()
        self.remaining_time = QTime(0,0)
        self.update_time_display()
        self.time_edit.setEnabled(True)

    def stop_timer(self):
        self.main_timer.stop()
        self.time_edit.setEnabled(False)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
