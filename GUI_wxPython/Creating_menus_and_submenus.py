# It's time to create the first interface element – the menu.  
# Three classes are used to create it:

# MenuBar – to create a menu bar;
# Menu – to create a menu tab;
# MenuItem – to create a separate item.

import wx

APP_EXIT = 1

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        # item = wx.MenuItem(fileMenu, wx.ID_EXIT, "Exit", "Exiting the application")
        # fileMenu.Append(item)

        item = fileMenu.Append(wx.ID_EXIT, "Exit\tCtrl+Q", "Exit the application")

        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, item)

    def onQuit(self, event):
        self.Close()

app = wx.App()
wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
