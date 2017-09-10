#! /usr/bin/env python3

import wx
import wx.html2

import os


class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		
		#Size at startup
		t=wx.Display()
		s = t.GetClientArea().GetSize()
		s.Height = s.Height * 2//3
		s.Width = s.Width*2//3
		
		wx.Frame.__init__(self, parent, title=title, size=s) 
		self.control=wx.html2.WebView.New(self) 
		self.CreateStatusBar() 
		
		icon = wx.Icon()
		icon.CopyFromBitmap(wx.Bitmap("includes/icon.ico", wx.BITMAP_TYPE_ANY))
		self.SetIcon(icon)
		   
		self.Centre()
		
		self.Show(True)
	
app = wx.App(False)
frame = MainWindow(None, title="Barluath")

# Toolbar	
toolbar = frame.CreateToolBar(name="Toolbar")
toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Folder.png").Rescale(32,32)), shortHelp="Open a new file")
toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/File.png").Rescale(32,32)), shortHelp="Save as PDF")
toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Cursor.png").Rescale(32,32)), shortHelp="Open editor")
toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Book.png").Rescale(32,32)), shortHelp="Tunebook options")
toolbar.AddStretchableSpace()
toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Gear.png").Rescale(32,32)), shortHelp="Settings")
toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Bang.png").Rescale(32,32)), shortHelp="Help & About")
toolbar.Realize()

welcome_html_file = open("includes/welcome.html")
welcome_html = welcome_html_file.read()
welcome_html_file.close()
frame.control.SetPage(html=welcome_html, baseUrl="")

app.MainLoop()
