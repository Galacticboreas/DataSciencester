# It's time to create the first interface element – the menu.  
# Three classes are used to create it:

# MenuBar – to create a menu bar;
# Menu – to create a menu tab;
# MenuItem – to create a separate item.

import wx

APP_EXIT = 1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        expMenu = wx.Menu()
        expMenu.Append(wx.ID_ANY, "Export image")
        expMenu.Append(wx.ID_ANY, "Export vide")
        expMenu.Append(wx.ID_ANY, "Export data")

        fileMenu.Append(wx.ID_NEW, '&New\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Open\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Save\tCtrl+S')
        fileMenu.AppendSubMenu(expMenu, "&Export")
        fileMenu.AppendSeparator()

        item = wx.MenuItem(fileMenu, APP_EXIT, "Exit\tCtrl+Q", "Exiting the application")
        fileMenu.Append(item)

        viewMenu = wx.Menu()
        viewMenu.Append(VIEW_STATUS, "Status bar", kind=wx.ITEM_CHECK)
        viewMenu.Append(VIEW_RGB, "Type RGB", "Type RGB", kind=wx.ITEM_RADIO)
        viewMenu.Append(VIEW_SRGB, "Type sRGB", "Type sRGB", kind=wx.ITEM_RADIO)

        # item = fileMenu.Append(wx.ID_EXIT, "Exit\tCtrl+Q", "Exit the application")

        menubar.Append(fileMenu, "&File")
        menubar.Append(viewMenu, "&Type")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)

    def onQuit(self, event):
        self.Close()

app = wx.App()
wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
