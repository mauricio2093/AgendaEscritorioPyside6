from PySide6.QtWidgets import QTableWidgetItem, QWidget, QTableWidgetItem, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
from PySide6 import QtWidgets


from views.main_window import MainWindow
from controllers.add_window import AddWindowForm
from controllers.edit_window import EditWindowForm
from controllers.recipe_details_window import DetailWindowForm
from views.general_custom_ui import GeneralCustomUi
from views import   components 

from database import recipes

class MainWindowForm(QWidget, MainWindow):

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.config_table()
        self.populate_table()

        self.new_recipi_button.clicked.connect(self.open_add_window)

    def mousePressEvent(self, event) :
        self.ui.mouse_press_event(event)

    def open_add_window(self):
        window = AddWindowForm()
        window.show()

    def open_edit_window(self, recipe_id):
        window = EditWindowForm(self, recipe_id)
        window.show()

    def config_table(self):
        colum_labels = ("ID", "IMG", "TITULO", "CATEGORIA","","FECHA")
        self.tableWidget.setColumnCount(len(colum_labels))
        self.tableWidget.setHorizontalHeaderLabels(colum_labels)
        stylesheet = "::section{Background-color:rgb(53, 53, 53); color:rgb(220,220,220);font-weight: bolder}"
        self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(150)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        
        self.tableWidget.verticalHeader().setVisible(False)

    def populate_table(self):
        data = recipes.select_all()

        self.tableWidget.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                if index_cell == 1:
                    self.tableWidget.setCellWidget(
                        index_row, index_cell, components.RecipeImg(cell)
                    )
                else:
                    self.tableWidget.setItem(
                        index_row, index_cell, QTableWidgetItem(str(cell))
                    )
            self.tableWidget.setCellWidget(
                index_row, 4, self.build_action_buttons()
            )

    def build_action_buttons(self):
        view_button = components.Button("view", "rgb(53,53,53)")
        edit_button = components.Button("edit", "rgb(7, 255, 119)")
        delete_button = components.Button("delete", "rgb(255, 17, 80)")


        button_layout = QHBoxLayout()
        button_layout.addWidget(view_button)
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)

        buttons_frame =  QFrame()
        buttons_frame.setLayout(button_layout)

        view_button.clicked.connect(self.view_recipe)
        edit_button.clicked.connect(self.edit_recipe)

        return buttons_frame

    def open_detail_window(self, recipe_id):
        window = DetailWindowForm(self, recipe_id)
        window.show()

    def view_recipe(self):
        button = self.sender()
        table = self.tableWidget

        if button:
            recipe_id = self.get_recipe_id_from_table(table, button)
            self.open_detail_window(recipe_id)

    def edit_recipe(self):
        button = self.sender()
        table = self.tableWidget

        if button:
            recipe_id = self.get_recipe_id_from_table(table, button)
            self.open_edit_window(recipe_id)
    

    def get_recipe_id_from_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index, 0)
        recipe_id = table.model().data(cell_id_index)
        return recipe_id