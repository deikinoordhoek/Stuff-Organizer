import gtk
import cairo
import listfiles
import gobject
class FileView(gtk.DrawingArea):
	def __init__(self):
		self.current_path = "/home/victor/"
		gtk.DrawingArea.__init__(self)		
		self.connect("expose_event", self.expose)
		self.file_lister = listfiles.FileLister(self.current_path)		
	def expose(self, widget, data=None):
		cr = self.window.cairo_create()
		self.draw(cr, *self.window.get_size())
	def draw(self, cr, width, height):
	        linear = cairo.LinearGradient(0, 0, 0, height)
	        linear.add_color_stop_rgba(0.00,  1, 1, 1, 1)
	        linear.add_color_stop_rgba(1.00,  0.9, 0.9, 0.9, 1)	
		cr.set_source(linear)	
		cr.rectangle(0, 0, width, height)	
		cr.fill()
		self.draw_files(cr, width, height)
	def draw_files(self, cr, width, height):
		self.filelist = self.file_lister.get_list()
		cr.set_source_rgb(0,0,0)		
		y = 10 #Compensate for that it adds 100 at the start of the the first loop.
		x = -95
	        cr.select_font_face("Times New Roman", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
		cr.set_font_size(16)
		icon_theme = gtk.icon_theme_get_default()


		for filename in self.filelist:
			icon_name = self.file_lister.get_icon_name(filename)			
			try:
				pixbuf = icon_theme.load_icon(icon_name, 96, 0)
			except gobject.GError, exc:
				print "can't load icon", exc
				try:
					pixbuf = icon_theme.load_icon("unknown", 96, 0)
				except gobject.GError, exc:
					print "Massive icon FAIL"
					
			x = x + 100
			if x > width:
				x = -95
				y = y + 120			
			cr.set_source_pixbuf(pixbuf,x,y)			
			cr.paint()			
			cr.set_source_rgb(0,0,0)		
			cr.move_to(x + 10, y + 110)
			cr.show_text(filename)
			
