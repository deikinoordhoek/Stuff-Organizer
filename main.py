#! /usr/bin/env python
import gtk
import cairo
import window
main = window.MainWindow()
main.connect("delete-event", gtk.main_quit)
main.show()
gtk.main()
