# Importa o QtCore
from ..qt_core import *

class UI_MainWindow(object):

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
        self.view_port.setGeometry(0, 0, 640, 440)

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
        
        if self.viewport is not None:
            self.render_objects()
        else:
            print("Fez nada")
    

    def render_objects(self):
        self.resize_viewport()
        self.show_objects()

    
    def resize_viewport(self):
        print("Resize ViewPort")
        d = self.viewport.get_vpmax()
        self.view_port.setGeometry(0, 0, d[0], d[1])
    

    def show_objects(self):
        for obj in self.objects:
            print(obj)

    """
    def set_viewport(self):
        green_Brush = QBrush(Qt.green)
        black_pen = QPen(Qt.black)
        black_pen.setWidth(5)
        ellipse = self.view_objects.addEllipse(10, 10, 200, 200, black_pen)
    """