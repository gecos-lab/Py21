from FracturedPy.GUI.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


import pyvista as pv
from pyvistaqt import QtInteractor as pvQtInteractor
from vtkmodules.vtkInteractionWidgets import vtkCameraOrientationWidget


class ProjectWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(ProjectWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.plotter = None
        self.cam_orient_widget = None
        self.default_view = None
        self.initialize_interactor()
        self.show_qt_canvas()

    def initialize_interactor(self):

        self.plotter = pvQtInteractor(self)
        self.plotter.set_background(
            "gray"
        )
        self.VtkLayout.addWidget(self.plotter.interactor)

        """Set orientation widget (turned on after the qt canvas is shown)"""
        self.cam_orient_widget = vtkCameraOrientationWidget()
        self.cam_orient_widget.SetParentRenderer(self.plotter.renderer)

        """Manage home view"""
        self.default_view = self.plotter.camera_position

        self.plotter.track_click_position(
            lambda pos: self.plotter.camera.SetFocalPoint(pos), side="left", double=True
        )

    def show_qt_canvas(self):
        """Show the Qt Window"""
        self.show()
        self.cam_orient_widget.On()
