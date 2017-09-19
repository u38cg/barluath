#! /usr/bin/env python3

import wx
import wx.html2

import os

import parser
import engraver

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		
		debug = True
		
		#Size at startup
		t=wx.Display()
		s = t.GetClientArea().GetSize()
		s.Height = s.Height * 2//3
		s.Width = s.Width*2//3
		
		wx.Frame.__init__(self, parent, title=title, size=s) 
		self.html_area = wx.html2.WebView.New(self) 
		self.CreateStatusBar() 
		
		icon = wx.Icon()
		icon.CopyFromBitmap(wx.Bitmap("includes/icon.ico", wx.BITMAP_TYPE_ANY))
		self.SetIcon(icon)
		
		# Toolbar	
		toolbar = self.CreateToolBar(name="Toolbar")
		tb_open = toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Folder.png").Rescale(32,32)), shortHelp="Open a new file")
		toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/File.png").Rescale(32,32)), shortHelp="Save as PDF")
		toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Cursor.png").Rescale(32,32)), shortHelp="Open editor")
		toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Book.png").Rescale(32,32)), shortHelp="Tunebook options")
		toolbar.AddStretchableSpace()
		if debug:
			tb_dump = toolbar.AddTool(-1, label="dump", bitmap=wx.Bitmap(wx.Image("includes/Bang.png").Rescale(32,32)), shortHelp="Dump parse tree")
		toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Gear.png").Rescale(32,32)), shortHelp="Settings")
		toolbar.AddTool(-1, label="", bitmap=wx.Bitmap(wx.Image("includes/Bang.png").Rescale(32,32)), shortHelp="Help & About")
		toolbar.Realize()
		
		#Toolbar bindings
		self.Bind(wx.EVT_TOOL, self.FileOpen, tb_open)
		if debug:
			self.Bind(wx.EVT_TOOL, self.Dump, tb_dump)
		self.Centre()
		
		self.Show(True)
		
		#Initialise engraver
		self.engraver = engraver.Engraver()
		
	def FileOpen(self, event):
		dialog = wx.FileDialog(self, "Choose a file")
		if dialog.ShowModal() == wx.ID_OK:
			f = open(dialog.GetPath(), 'r')
			file_contents = f.read()
			f.close()
			self.Engrave(file_contents)
	
	def Engrave(self, file_contents):
		parse_result = parser.tunefile.parseString(file_contents)
		self.engraver.SetTuneFile( parse_result )
		self.html_area.SetPage(html=self.engraver.html, baseUrl="")
		
	def Dump(self, event):
		print(self.engraver.tunefile.dump())
		
app = wx.App(False)
frame = MainWindow(None, title="Barluath")

welcome_html_file = open("includes/welcome.html")
welcome_html = welcome_html_file.read()
welcome_html_file.close()
frame.html_area.SetPage(html=welcome_html, baseUrl="")

app.MainLoop()
