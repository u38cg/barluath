class Engraver:
	def __init__(self):
		self.html="Initiated with no tunefile"
	def SetTuneFile(self,  tunefile):
		if tunefile is not None:
			self.html = "<pre>" + tunefile.dump() + "</pre>"
