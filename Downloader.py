#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.5 on Thu Mar 13 16:50:43 2008

import wx
import global_var,MainFrame

class AppDownloader(wx.App):
    
    def __init__(self, redirect=True, filename=None):
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        self.frame = MainFrame.MainFrame(None, -1, "") 
        self.frame.Show() 
        self.SetTopWindow(self.frame)
        return True
if __name__ == "__main__":
    app = AppDownloader(0)
    wx.InitAllImageHandlers()
    app.MainLoop()