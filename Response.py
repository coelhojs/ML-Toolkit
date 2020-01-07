class Response: 
    RequestId = ""
    Method = ""
    Model = ""
    Results = []

    # default constructor 
    def __init__(self, requestId, method, model): 
        self.RequestId = requestId
        self.Method = method
        self.Model = model
        self.Results = []


    def add_results(self, image_path, results): 
        self.Results.append('{image_path}:{results}'.format(image_path=image_path,results=results))


    def set_results(self, results):
        self.Results = results