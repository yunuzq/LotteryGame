from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from PyQt5.QtGui import* 
from random import randint


app=QApplication([])
                 

my_win=QWidget()

my_win.setWindowTitle("Milli piyango")
my_win.resize(400,200)

button=QPushButton('Oluştur')
text=QLabel("Tıkla ve Kazan")   
sayi=QLineEdit()                                                                                                                                                                                                                           
winner=QLabel("?")
winner.setFont(QFont("Arial", 25))


my_win.setStyleSheet("Background-color: red")
button.setStyleSheet("color: yellow")
sayi.setStyleSheet("Background-color: white")
text.setStyleSheet("color: yellow")
winner.setStyleSheet("color: white",)



line=QVBoxLayout()
line.addWidget(text,alignment=Qt.AlignCenter)
text.setFont(QFont("Arial", 20))
line.addWidget(winner,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)
line.addWidget(sayi,alignment=Qt.AlignCenter)
tahmin=sayi.text()
print(tahmin)
my_win.setLayout(line)


def show_winner():
    number=randint(0,5)
    print(number)
    
    tahmin=int(sayi.text())
    
    if(number==tahmin):
        winner.setText(str(number)) 
        text.setText("Winner:")
    else:
        text.setText("Tekrar dene:")


button.clicked.connect(show_winner)



my_win.show()
app.exec_()