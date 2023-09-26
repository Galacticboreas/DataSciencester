import wx

app = wx.App()

frame = wx.Frame(None, title='Hello, World!')
# In the constructor of the Frame class, we specify 
# three parameters:

# parent – a reference to the parent window 
#    (if there is none, then None is specified, 
#    then the window becomes the main window of 
#    the application);
# id is the unique identifier of the widget 
#    (by specifying wx.ID_ANY we say that it is 
#    formed automatically);
# title – the title of the window.
frame.Show()
app.MainLoop()

wnd = wx.Frame(None, wx.ID_ANY, "Hello World!", size=(500, 200),
          style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
wnd.Show()
app.MainLoop()

wnd = wx.Frame(None, wx.ID_ANY, "Hello World!", size=(500, 200), pos = (100,0))
wnd.Show()
app.MainLoop()

wnd = wx.Frame(None, wx.ID_ANY, "Hello World!", size=(500, 200))
wnd.Centre()
wnd.Show()
app.MainLoop()

# We will get a window in the center. The following 
# useful methods of the Frame class are also available:

# Close() – closes the window;
# Maximize() – opens the window to full screen;
# Move(x, y) – positions the window with an offset of x, y 
# pixels from the upper left corner of the screen;
# setPosition( pt: wx.Point ) – places a window with the 
# starting point pt, for example, 
# wnd.setPosition( wx.Point(100, 500) );
# setSize(x, y, width, height) – sets the position and size 
# of the window.
