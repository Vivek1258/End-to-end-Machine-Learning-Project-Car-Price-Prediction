

### Python script to perform 
### Feature Scealing 

import pickle 

def load_file(filename):
        with open(filename , 'rb') as f:
            x = pickle.load(f)
        return x['Normalization_Params']

class transformer(object):

    def __init__(self, m_path = "train/meta_data" ):
        super(transformer, self).__init__()
        self.mata_data = load_file(m_path)
        # print(self.mata_data)

    def norm_Present_Price(self, Present_Price):
    	return (Present_Price - self.mata_data['min_present_price'] ) / (  self.mata_data['max_present_price'] - self.mata_data['min_present_price'])


    def norm_Kms_Driven(self, Kms_Driven):
    	return ( Kms_Driven - self.mata_data['min_kms_driven'] ) / (  self.mata_data['max_kms_driven'] - self.mata_data['min_kms_driven'])

    def norm_Years_used(self, Years_used):
        return (Years_used - self.mata_data['min_years_used'] ) / (  self.mata_data['max_years_used'] - self.mata_data['min_years_used'])

    def de_norm_Selling_Price(self, Selling_Price):
    	return (Selling_Price*(  self.mata_data['max_selling_price'] - self.mata_data['min_selling_price']) ) + self.mata_data['min_selling_price'] 
