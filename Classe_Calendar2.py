from codigo_calendario import Calendar
import tkinter as Tkinter
import calendar

#Coloca calendário e data selecionada

class Calendar2(Calendar):
    def __init__(self, master=None, data=None, **kw):
	
        from codigo_calendario import Calendar
		
        Calendar.__init__(self, master, **kw)
        self.quando_selecionada(data)

    def quando_selecionada(self, a_fun):
         self.data = a_fun


    def _pressed(self, evt):
        Calendar._pressed(self, evt)
        x = self.selection
        if self.data:
            self.data(x)