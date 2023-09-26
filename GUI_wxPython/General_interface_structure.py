import wx

# Here is a typical approach to the layout of interface elements 
# in the program window. And so that we can modify the Frame class, 
# it is more convenient to create our own by inheriting it from 
# the base Frame, for example, like this:

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

# Here we declare our constructor with two parameters: parent and 
# title, and then, inside it, we call the constructor of the base 
# class using the super() function. Further, according to the program, 
# we can use our class as follows:

app = wx.App()
 
wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()

# Of course, the Frame class is just one of the representatives of 
# window classes. There are six of them in wxPython and they are as 
# follows:

# PopupWindow is a special window class for creating popup menus, 
# combobox lists and other auxiliary widgets of this kind;
# ScrolledWindow – used to create a window with scrollable content;
# Frame – used to create a standard window;
# MDIParentFrame (Multiple Document Interface) – a class containing 
# child window classes (as an example, Photoshop with many open 
# documents);
# MDIChildFrame – creates a window inside the MDIParentFrame class;
# Dialog – creates a dialog box.

# For example, replace the standard window Frame with MDIParentFrame:

class MyFrame(wx.MDIParentFrame ):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)

        # And, then, add a child window using the MDIChildFrame class:
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)
        win = wx.MDIChildFrame(self, -1, "Child Window", size=(200, 150))
        win.Show()

wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()

# Further, when creating Layout, in addition to the Panel class, you 
# can also use such containers for widgets:

# ScrolledWindow – container with scrollable content;
# SplitterWindow is a container with a dividing strip that can be moved 
# by resizing the corresponding contents;
# Notebook – used to create a tab interface (a panel with tabs).
# Well, the basic set of widgets is defined by such classes:

# - for dynamic (i.e. their contents may change):

# Button – a regular button;
# BitmapButton – a button with a picture;
# ToggleButton – switch button;
# SpinButton – up/down arrows;
# RadioButton – radio button (circle with dot);
# CheckBox – checkbox (checkbox);
# TextCtrl – text input field;
# SpinCtrl – input field with up/down arrows;
# ComboBox – a drop-down list with the ability to enter a value;
# Choice – a drop-down list with only a choice;
# Slider – slider;
# ScrollBar – scrolling;
# Grid – table (similar to Excel);
# RadioBox – container for RadioButton;
# ListBox – a list.
# - for static:

# StaticBitmap – for static images;
# StaticBox – square frame;
# Gauge – progress bar;
# StaticText – plain text;
# StaticLine – a line.