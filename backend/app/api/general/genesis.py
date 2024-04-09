from fastapi import APIRouter
import pandas as pd

gen_router = APIRouter()

@gen_router.get('/test')
async def test():
    return {"message": "Hello World"}

@gen_router.get('/getData')
async def getData():
    # df = pd.read_csv("D:\Anandu\projects\capstone_v1\backend\app\api\general\Data.csv ")
    fileName = r'D:\Anandu\projects\capstone_v1\backend\app\api\general\Data.csv'
    df= pd.read_csv(fileName)

    province_population = df.groupby('Province')['Population'].sum()
        
        # Calculate the total population
    total_population = province_population.sum()
        
        # Calculate the percentage of total population for each province
    province_population_percentage = (province_population / total_population) * 100
    province_population_percentage_dict = province_population_percentage.to_dict()
    province_names = list(province_population_percentage_dict.keys())
    province_pop_percent = list(province_population_percentage_dict.values())
    print(province_names)
    print("*"*20)
    print(province_pop_percent)
    return {"message": {
        "province": province_names,
        "pop_percent": province_pop_percent
    }}
