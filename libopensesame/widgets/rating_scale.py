#-*- coding:utf-8 -*-

"""
This file is part of openexp.

openexp is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

openexp is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with openexp.  If not, see <http://www.gnu.org/licenses/>.
"""

from widget import widget
from box_widget import box_widget

class rating_scale(widget, box_widget):

	"""A simple rating scale/ Likert widget"""

	def __init__(self, form, nodes=5, click_accepts=False):
	
		"""<DOC>
		Constructor
		
		Arguments:
		form -- the parent form
		
		Keyword arguments:
		nodes -- the number of nodes or a list of node identifiers (e.g.,
				 ['yes', 'no', 'maybe']. If a list is passed the rating scale
				 will have labels, otherwise it will just have boxes.
				 (default=5)
		click_accepts -- indicates whether the form should close when a value
						 is selected (default=False)
		</DOC>"""	
		
		widget.__init__(self, form)
		box_widget.__init__(self)
		self.type = 'rating_scale'
		self.box_size = 16
		self.value = None
		self.click_accepts = click_accepts
		self.pos_list = []
		if type(nodes) == int:
			self.nodes = ['']*nodes
		else:
			self.nodes = nodes
			
	def on_mouse_click(self, pos):
	
		"""<DOC>
		Is called whenever the user clicks on the widget. Selects the correct
		value from the scale and optionally closes the form.
		
		Arguments:
		pos -- an (x, y) tuple		
		</DOC>"""		
	
		x, y = pos
		i = 0
		for _x, _y in self.pos_list:
			if x >= _x and x <= _x+self.box_size and y >= _y and y <= \
				_y+self.box_size:
				if self.click_accepts:												
					return i				
				self.value = i
				break
			i += 1
		
	def render(self):
	
		"""<DOC>
		Draws the widget
		</DOC>"""	
	
		x, y, w, h = self.rect		
		w -= self.box_size		
		cy = y+h/2
		dx = 1*w/(len(self.nodes)-1)						
		self.form.canvas.line(x, cy, x+w, cy)		
		_x = x
		i = 0
		for node in self.nodes:
			self.draw_box(self.value == i, _x, cy)
			text_height = self.form.canvas.text_size(node)[1]
			self.form.canvas.text(node, center=True, x=_x+self.box_size/2, \
				y=cy-text_height/2)						
			self.pos_list.append( (_x, cy) )
			_x += dx
			i += 1