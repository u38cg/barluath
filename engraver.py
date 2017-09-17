class Engraver:
	def __init__(self, tunefile):
		self.html = "<pre>" + tunefile.dump() + "</pre>"
		
