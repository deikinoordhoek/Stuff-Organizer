import gtk
class MainToolbar(gtk.VBox):
	def __init__(self):
		gtk.VBox.__init__(self)
		self.go_button = gtk.Button("Go!")
		self.vseparator = gtk.HSeparator()
		self.hbox = gtk.HBox()
		self.hbox.pack_start(self.go_button, False, False)
		
		self.pack_start(self.hbox, False, False)
		self.pack_start(self.vseparator, False, False)		

		self.go_button.show()
		self.vseparator.show()
		self.hbox.show()
