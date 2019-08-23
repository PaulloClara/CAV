import tkinter as tk


class GUI(tk.Frame):
  def __init__(self):
    master = tk.Tk()
    super().__init__(master)
    self.master = master

  def show(self, msg):
    print(msg)

  def get(self, msg):
    return input(msg)

  def start(self):
    self.master.title('CAV - Clara Assistente Virtual')
    self.pack()
    self.create_widgets()
    self.mainloop()

  def create_widgets(self):
    self.to_ask = tk.Button(self)
    self.to_ask['text'] = 'Falar'
    self.to_ask['command'] = self.hi
    self.to_ask.pack(side='top')
    self.quit = tk.Button(self)
    self.quit['text'] = 'Sair'
    self.quit['fg'] = 'red'
    self.quit['command'] = self.master.destroy
    self.quit.pack(side='bottom')

  def hi(self):
    print('hi there, everyone!')
