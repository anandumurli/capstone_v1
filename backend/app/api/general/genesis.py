from fastapi import APIRouter
import pandas as pd

gen_router = APIRouter()

@gen_router.get('/test')
async def test():
    return {"message": "Hello World"}

@gen_router.get('/getSumPopulation')
async def getSumPopulation():
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

@gen_router.get('/getSumPrice')
async def getSumPrice():
    fileName = r'D:\Anandu\projects\capstone_v1\backend\app\api\general\Data.csv'
    df= pd.read_csv(fileName)
    province_price = df.groupby('Province')['Price'].sum()
    province_price_dict = province_price.to_dict()
    province_names = list(province_price_dict.keys())
    province_price_total = list(province_price_dict.values())
    return {"message": {
        "province": province_names,
        "pop_price": province_price_total
    }}

@gen_router.get('/getTopCities')
async def getTopCities():
    fileName = r'D:\Anandu\projects\capstone_v1\backend\app\api\general\Data.csv'
    df= pd.read_csv(fileName)
    city_population = df.groupby('City')['Population'].sum()
    city_population_sorted_dict = city_population.sort_values(ascending=False).head(7).to_dict()
    city_names = list(city_population_sorted_dict.keys())
    city_population_total = list(city_population_sorted_dict.values())
    return {"message": {
        "cities": city_names,
        "city_pop": city_population_total
    }}