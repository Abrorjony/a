import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window(title="Hello")
win.connect("destroy", Gtk.main_quit)
label = Gtk.Label(label="Hello")
win.add(label)
win.show_all()
Gtk.main()
