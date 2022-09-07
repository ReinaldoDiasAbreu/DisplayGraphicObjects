# Importa o QtCore
from ctypes import POINTER
from nis import match
from tkinter import W
from ..qt_core import *

WIDTH_PEN = 3

class UI_MainWindow(object):

    def __init__(self) -> None:
        self.window_data = None
        self.viewport = None
        self.objects = None

    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # Parametros Iniciais
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # Criando um Frame Central
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")

        # Criando main layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0) # Remove bordas entre os frames
        self.main_layout.setSpacing(0) # Remove espaçamento central

        # Criando Left Menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(200)
        self.left_menu.setMinimumWidth(200)

        # Criando Left Menu Layout
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)
        
        # Criando Top Frame do Menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        #self.left_menu_top_frame.setStyleSheet("background-color: #ffffff")
        self.left_menu_top_frame_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_frame_layout.setSpacing(0)

        # Criando botões do Top Frame Menu
        self.btn_open_file = QPushButton("Open File", self.left_menu)
        self.left_menu_top_frame_layout.addWidget(self.btn_open_file)

        self.btn_save_file = QPushButton("Save Coords", self.left_menu)
        self.left_menu_top_frame_layout.addWidget(self.btn_save_file)
        
        # Espaçador do Menu
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Criando Bottom Frame do Menu
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        #self.left_menu_bottom_frame.setStyleSheet("background-color: #ffffff")

        # Criando Label Version
        self.left_menu_bottom_frame_label_version = QLabel("v 1.0.0")
        self.left_menu_bottom_frame_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_bottom_frame_label_version.setMinimumHeight(30)
        self.left_menu_bottom_frame_label_version.setMaximumHeight(30)
        self.left_menu_bottom_frame_label_version.setStyleSheet("color: #c3ccdf")

        # Adicionando objetos ao layout do menu
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame_label_version)

        # Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # Adicionando Frames ao Main Layout
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Criando Barra Superior
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)
        self.top_bar_layout.setSpacing(0)
        
        # Widgets barra superior
        self.top_label_left = QLabel("Viewport Objects")
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.top_label_right = QLabel("COMPUTAÇÃO GRÁFICA")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # Adicionando Widges na barra superior
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # Criando página de Conteudo
        self.pages = QFrame()
        self.pages.setStyleSheet("font-size: 12pt; color: #ffffff")
        self.pages_style = QVBoxLayout(self.pages)
        self.pages_style.setContentsMargins(0, 0, 0, 0)
        self.pages_style.setSpacing(0)

        # Criando ViewPort
        self.view_objects = QGraphicsScene(self.pages)

        # Inserindo ViewObjects em Pages
        self.view_port = QGraphicsView(self.view_objects, self.pages)
        #self.view_port.setGeometry(0, 0, 900, 500)
        self.view_port.setAlignment(Qt.AlignCenter)
        self.view_port.adjustSize()

        # Criando Barra Inferior
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)
        self.bottom_bar_layout.setSpacing(0)
        
        # Widgets barra superior
        self.bottom_label_left = QLabel("")
        self.bottom_label_left.setStyleSheet("font-size: 10pt; color: #ffffff")
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.bottom_label_right = QLabel("Criado por: Reinaldo Junio Dias")
        self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # Adicionando Widges na barra superior
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # Adicionando TopBar e Pages ao Content Layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Set central frame
        parent.setCentralWidget(self.central_frame)
    
    
    def define_objects(self, window_data=None, viewport_data=None, objects_data=None):
        self.window_data = window_data
        self.viewport = viewport_data
        self.objects = objects_data

        print(self.objects)
        
        if self.viewport is not None:
            self.render_objects()
    

    def render_objects(self):
        self.show_objects()

    
    def resize_viewport(self):
        self.view_objects.clear()
        self.view_objects.update()
        w = 640
        h = 440

        if self.viewport is not None:
            vpmax = self.viewport.get_vpmax()
            vpmin = self.viewport.get_vpmin()
            w = vpmin[0] + vpmax[0]
            h = vpmin[1] + vpmax[1]

        # Adicionando retângulo de borda
        janela = QRectF()
        janela.setRect(0, 0, w, h)
        self.view_objects.addRect(janela)
        
        print("Resize ViewPort to:", self.view_port.rect())
        self.view_port.setGeometry(0, 0, w+10, h+10)
        self.view_port.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)


    
    def convert_x_to_xvp(self, XW, wmin, wmax, vpmin, vpmax):
        return ( (XW - wmin[0])/(wmax[0] - wmin[0]) ) * ( vpmax[0] - vpmin[0] )


    def convert_y_to_yvp(self, YW, wmin, wmax, vpmin, vpmax):
        return ( 1 - ((YW - wmin[1])/(wmax[1] - wmin[1])) ) * ( vpmax[1] - vpmin[1] )


    def show_objects(self):
        wmin = self.window_data.get_wmin()
        wmax = self.window_data.get_wmax()
        vpmin = self.viewport.get_vpmin()
        vpmax = self.viewport.get_vpmax()

        self.resize_viewport()

        for obj in self.objects:

            str_type = str(type(obj))
            if str_type == "<class 'dgo.objects.ponto.Ponto'>": self.show_ponto(obj, wmin, wmax, vpmin, vpmax)
            elif str_type == "<class 'dgo.objects.reta.Reta'>": self.show_reta(obj, wmin, wmax, vpmin, vpmax)
            elif str_type == "<class 'dgo.objects.poligono.Poligono'>": self.show_poligono(obj, wmin, wmax, vpmin, vpmax)
            self.view_objects.update()


    def show_ponto(self, obj, wmin, wmax, vpmin, vpmax):
        xw = obj.get_x()
        yw = obj.get_y()
        xvp = self.convert_x_to_xvp(xw, wmin, wmax, vpmin, vpmax)
        yvp = self.convert_y_to_yvp(yw, wmin, wmax, vpmin, vpmax)

        print(f"Ponto: [{xvp}, {yvp}].")

        green_pen = QPen(Qt.green)
        green_pen.setWidth(WIDTH_PEN+2)
        green_brush = QBrush(Qt.green)

        self.view_objects.addEllipse(xvp, yvp, 1, 1, green_pen, green_brush)
    

    def show_reta(self, obj, wmin, wmax, vpmin, vpmax):
        points = obj.get_list_points()

        xvp1 = self.convert_x_to_xvp(points[0][0], wmin, wmax, vpmin, vpmax)
        yvp1 = self.convert_y_to_yvp(points[0][1], wmin, wmax, vpmin, vpmax)
        xvp2 = self.convert_x_to_xvp(points[1][0], wmin, wmax, vpmin, vpmax)
        yvp2 = self.convert_y_to_yvp(points[1][1], wmin, wmax, vpmin, vpmax)

        print(f"Reta: [{xvp1}, {yvp1}] - [{xvp2}, {yvp2}].")

        red_pen = QPen(Qt.red)
        red_pen.setWidth(WIDTH_PEN)

        self.view_objects.addLine(xvp1, yvp1, xvp2, yvp2, red_pen)
    

    def show_poligono(self, obj, wmin, wmax, vpmin, vpmax):
        points = obj.get_list_points()
        poligono = QPolygonF()

        blue_pen = QPen(Qt.blue)
        blue_pen.setWidth(WIDTH_PEN)

        print("Poligono: [", end="")

        for p in points:
            ponto = QPointF()
            xvp = self.convert_x_to_xvp(p[0], wmin, wmax, vpmin, vpmax)
            yvp = self.convert_y_to_yvp(p[1], wmin, wmax, vpmin, vpmax)
            ponto.setX(xvp)
            ponto.setY(yvp)
            print(f"({xvp}, {yvp}) ", end="")
            poligono.append(ponto)
        
        print("]")
        
        self.view_objects.addPolygon(poligono, blue_pen)

