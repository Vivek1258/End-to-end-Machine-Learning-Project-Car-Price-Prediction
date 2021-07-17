

### Python script to perform 
### Feature Scealing 

class transformer(object):

	"""docstring for transformer"""
	def __init__(self, m_path = "train/meta_data" ):
		super(transformer, self).__init__()
		self.mata_data = __load_file(m_path)


	def __load_file(filename):

		with open('filename', 'rb') as f:
    			x = pickle.load(f)

    	return x 

    def norm_Present_Price(Present_Price):
    	return (Present_Price - mata_data[min_present_price] ) / (  mata_data[max_present_price] - mata_data[min_present_price])


    def norm_Kms_Driven(Kms_Driven):
    	return ( Kms_Driven - mata_data[min_kms_driven] ) / (  mata_data[max_kms_driven] - mata_data[min_kms_driven])
	
    def norm_Years_used(Years_used):
    return (Years_used - mata_data[min_years_used] ) / (  mata_data[max_years_used] - mata_data[min_years_used])

    def de_norm_Selling_Price(Selling_Price):
    	return (Selling_Price*(  mata_data[max_selling_price] - mata_data[min_selling_price]) ) + mata_data[min_selling_price] 
