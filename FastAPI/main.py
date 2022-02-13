import uvicorn
import pickle
from joblib import dump, load
from fastapi import FastAPI
from features import Features,ID,conecction_mysql,find_


app = FastAPI()
#pickle_in = open("../Model/model_risk.joblib", "rb")
#model = pickle.load(pickle_in)

model = load('../Model/model_risk.joblib') 


@app.get('/')
def index():
    return {'message': 'This is the homepage of the Risk API '}


@app.post('/predict')
def get_status_risk(data: Features):
    
    """
    get_status_risk () 
    
    Parameters :
       
    
    
    Returns : 
    
    """
    

    received = data.dict()

    #Get features 
    age = received['age']
    years_on_the_job = received['years_on_the_job']
    nb_previous_loans = received['nb_previous_loans']
    avg_amount_loans_previous = received['avg_amount_loans_previous']
    flag_own_car = received['flag_own_car']


               
    pred_name = model.predict([[age, 
                                years_on_the_job,
                                nb_previous_loans,
                                avg_amount_loans_previous,
                                flag_own_car
                                ]]).tolist()[0]

    print("pred_name: ", pred_name)

    return {'prediction': pred_name}



@app.post('/get_features')
def get_features(data: ID):
    
    """
    get_features () get 5 features of  risk  model
    
    Parameters :
        
                ID : ID user
    
    
    Returns : 
                features =  {
                "age": feat['age],
                "years_on_the_job": feat[2],
                "nb_previous_loans": feat[1],
                "avg_amount_loans_previous":feat[3],
                "flag_own_car": feat[4],
            }
    
    """

    received = data.dict()

    #Get features 
    #age,nb_previous_loans,years_on_the_job,avg_amount_loans_previous,flag_own_car
    feat = find_(received['id'])

    features =  {
                "age": feat[0],
                "years_on_the_job": feat[2],
                "nb_previous_loans": feat[1],
                "avg_amount_loans_previous":feat[3],
                "flag_own_car": feat[4],
            }

    return {'features': features}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
