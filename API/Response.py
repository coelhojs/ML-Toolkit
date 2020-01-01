class Response: 
	RequestId = ""
    Method = ""
	Model = ""
    Results = []

	# default constructor 
	def __init__(requestId, method): 
		self.RequestId = requestId
        self.Method = method
        self.Results = []


	def add_results(image_path, results): 
		self.Results.append('{image_path}:{results}'.format(image_path=image_path,results=results))

	def set_results(results):
		self.Results = results