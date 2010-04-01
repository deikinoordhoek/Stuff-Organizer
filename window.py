import gtk
import toolbar
import file_view
class MainWindow(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_size_request(800,600)		
		
		self.top_toolbar = toolbar.MainToolbar()
		self.fileview = file_view.FileView()		
		self.main_vbox = gtk.VBox()

		self.main_vbox.pack_start(self.top_toolbar, False, False)
		self.main_vbox.pack_start(self.fileview)		
		self.add(self.main_vbox)

		self.main_vbox.show()
		self.top_toolbar.show()
		self.fileview.show()
