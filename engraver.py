class Engraver:
	def __init__(self):
		self.html="Initiated with no tunefile"
		self.preamble=	"""
						<html>
						<head><style>
													
						html {	background-color: #def2f9;
								padding: 2em;
								}
								
						p {		color: red;
								font-weight: bold;
								width: 50%;
								margin: auto;
								}	
									
						.content-page {	width: 210mm;
										height: 297mm;
										background-color: white;
										border-style: solid;
										border-width: 1px;
										box-shadow: 10px 10px 5px #888888;
										margin: auto;
									}
						</style></head>
						<body>"""
		self.postamble=	"""
						</body></html>"""
		
		
	def SetTuneFile(self,  tunefile):
		if tunefile is not None:
			self.html = 	(self.preamble + 
							"<div class=\"content-page\"><pre>")
			for i in range(0,len(tunefile)):
				block_type = list(tunefile[i].asDict())[0]
				self.html = self.html + block_type + "\n"
			self.html = self.html + "</pre></div>" + self.postamble
