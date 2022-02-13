from pydantic import BaseModel, Field
import psycopg2



def conecction_mysql():
    
        
    """
    conecction_mysql () 
    
    Parameters :
       
    
    
    Returns : 
    """
    conn = None
    try :
        #establishing the connection
        conn = psycopg2.connect(
                database="kueski",
                user='postgres',
                password='postgresmaster',
                host='127.0.0.1',#'172.17.0.4',
                port= '5432')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
          
    return conn


def find_(id_):
    
    """
    find_ () 
    
    Parameters :
       
    
    
    Returns : 
    """

    query = (
    "SELECT age,nb_previous_loans,years_on_the_job,avg_amount_loans_previous,flag_own_car "
    "FROM features "
    "WHERE id=%s " 
    "ORDER BY nb_previous_loans DESC "
    "LIMIT 1")


    conn = conecction_mysql()

    if conn is not None:
        cur = conn.cursor()
        
        cur.execute(query,(id_,)) 

        row = cur.fetchone()
        cur.close()
        conn.close()
        
    return row




class Features(BaseModel):
    
    
    """
    Features () 
    
    Parameters :
       
    
    
    Returns : 
    """
    
    
    
    age: int = Field(..., description="Here is the description of the input to be sent")
    years_on_the_job: int = Field(..., description="Here is the description of the input to be sent")
    nb_previous_loans: int = Field(..., description="Here is the description of the input to be sent")
    avg_amount_loans_previous: float = Field(..., description="Here is the description of the input to be sent")
    flag_own_car: int = Field(..., description="Here is the description of the input to be sent")
    class Config:
        schema_extra = {
            "example": {
                "age": 40,
                "years_on_the_job": 3,
                "nb_previous_loans": 12,
                "avg_amount_loans_previous": 138.568,
                "flag_own_car": 0,
            }
        }


class ID(BaseModel):
    
    """
    Features () 
    
    Parameters :
       
    
    
    Returns : 
    """
    
    
    id: int = Field(..., description="Here is the description of the input to be sent")

    class Config:
        schema_extra = {
            "example": {
                "id": 5008806,
            }
        }