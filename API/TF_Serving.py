class TF_Serving_Request: 
	Headers = {"content-type": "application/json"}
    Images = []
    Url = ""


	# default constructor 
	def __init__(requestId, method): 
		self.RequestId = requestId
        self.Detections = []


    def call_img_classification():
        print(f'\n\nMaking request to {server_url}...\n')
        for image_path in self.Images:
            # Converte o arquivo num float array
            formatted_json_input = img_util.classification_pre_process(image_path)
            server_response = requests.post(server_url, data=formatted_json_input, headers=headers)
            print(server_response)

            # Decoding results from TensorFlow Serving server
            pred = json.loads(server_response.content.decode('utf-8'))
            predictions = np.squeeze(pred['predictions'][0])
            results = []
            top_k = predictions.argsort()[-5:][::-1]
            labels = load_labels(label_file)
            for i in top_k:
                label = labels[i]
                score = float(predictions[i])
                results.append('{label},{score}'.format(label=label,score=score))
        print(f'Request returned\n')
        return results