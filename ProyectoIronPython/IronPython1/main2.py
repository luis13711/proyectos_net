import sys
sys.path.append(r'C:\Python24\Lib')

import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")

from System.Drawing import Point
from System.Windows.Forms import Application, Button, Form, Label

class HelloWorldForm(Form):

    def __init__(self):
        self.Text = 'Hello World'

        self.label = Label()
        self.label.Text = "Please Click Me"
        self.label.Location = Point(50, 50)
        self.label.Height = 30
        self.label.Width = 200

        self.count = 0

        button = Button()
        button.Text = "Click Me"
        button.Location = Point(50, 100)

        button.Click += self.buttonPressed

        self.Controls.Add(self.label)
        self.Controls.Add(button)

    def buttonPressed(self, sender, args):
        print 'The label *used to say* : %s' % self.label.Text
        self.count += 1
        self.label.Text = "You have clicked me %s times." % self.count


form = HelloWorldForm()
Application.Run(form)