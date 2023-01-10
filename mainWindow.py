from file_mover import Filemover
from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QCheckBox, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTextEdit, QGroupBox, QHBoxLayout
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.fm = Filemover()
        
        self.setWindowTitle("Sorter 1.0")       
        
        self.boxLayout = QVBoxLayout()
        #self.boxLayout = QHBoxLayout() 
         
        # Create group box for checkable items
        self.checkBoxGroup = QGroupBox("Choose items to sort")
        
        # Create layout for the group
        self.group_box_layout = QVBoxLayout()   
             
        # Set layout as groups layout
        self.checkBoxGroup.setLayout(self.group_box_layout)
       
        # Add checkboxgroup widget to mainlayout
        self.boxLayout.addWidget(self.checkBoxGroup)       
        
        self.path_to_folder()
        self.create_browse_btn()
        self.create_checkBox()
        self.create_sort_button()
        
        widget = QWidget()
        widget.setLayout(self.boxLayout)
        
        self.setCentralWidget(widget)
        
        
        # Creates checkboxes according to extensions directory from file_mover.py 
    def create_checkBox(self):
        self.checkbox_list = []
        for k in self.fm.extensions:
            self.ch_box = QCheckBox(k, self.checkBoxGroup)
            self.ch_box.setCheckState(Qt.CheckState.Unchecked)
            #self.ch_box.stateChanged.connect(self.check_checkbox_status)
            self.group_box_layout.addWidget(self.ch_box)
            #self.checkbox_list.append(self.ch_box)
            
        # Check status of checkboxes
    def check_checkbox_status(self):
        self.checked_list = []
        # Scans checkboxes in checkboxgroup and if it's status is checked puts it into a checked list.
        for checkbox in self.checkBoxGroup.findChildren(QCheckBox):
            if checkbox.isChecked():
                self.checked_list.append(checkbox.text())
        
        self.fm.scan_files(self.path, self.checked_list)
        
        # Create sort button
    def create_sort_button(self):
        self.btn= QPushButton("Sort")
        self.boxLayout.addWidget(self.btn)
        self.btn.clicked.connect(self.check_checkbox_status)
        
        # Create textbox for folder path
    def path_to_folder(self):    
        self.folder_path = QTextEdit("Select folder")
        self.folder_path.setMaximumHeight(30)
        self.boxLayout.addWidget(self.folder_path)
           
        # Create button to choose folder
    def create_browse_btn(self): 
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.browse_folder)
        self.boxLayout.addWidget(self.browse_btn)
      
        # Choose folder
    def browse_folder(self):
        self.folderName = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.path = self.folderName
        self.folder_path.setText(self.folderName)
        #self.ui.lineEdit.setText(folderName)
        
    
        
        