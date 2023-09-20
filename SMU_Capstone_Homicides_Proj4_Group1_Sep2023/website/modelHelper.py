import pandas as pd
import pickle

class modelHelper():
    def __init__(self):
        pass
    
    def makePredictions(age, year, population, sex, race, month, weekday, season, city, state):
        lgbm_model = pickle.load(open('model.pkl', 'rb'))
        inp = {'victim_age': 0,
            'reported_year': 0,
            'POPULATION': 0,
            'victim_sex_Female': 0,
            'victim_sex_Male': 0,
            'victim_race_Asian': 0,
            'victim_race_Black': 0,
            'victim_race_Hispanic': 0,
            'victim_race_Other': 0,
            'victim_race_White': 0,
            'reported_month_April': 0,
            'reported_month_August': 0,
            'reported_month_December': 0,
            'reported_month_February': 0,
            'reported_month_January': 0,
            'reported_month_July': 0,
            'reported_month_June': 0,
            'reported_month_March': 0,
            'reported_month_May': 0,
            'reported_month_November': 0,
            'reported_month_October': 0,
            'reported_month_September': 0,
            'reported_weekday_Friday': 0,
            'reported_weekday_Monday': 0,
            'reported_weekday_Saturday': 0,
            'reported_weekday_Sunday': 0,
            'reported_weekday_Thursday': 0,
            'reported_weekday_Tuesday': 0,
            'reported_weekday_Wednesday': 0,
            'season_Fall': 0,
            'season_Spring': 0,
            'season_Summer': 0,
            'season_Winter': 0,
            'city_Albuquerque': 0,
            'city_Atlanta': 0,
            'city_Baltimore': 0,
            'city_Baton_Rouge': 0,
            'city_Birmingham': 0,
            'city_Boston': 0,
            'city_Buffalo': 0,
            'city_Charlotte': 0,
            'city_Chicago': 0,
            'city_Cincinnati': 0,
            'city_Columbus': 0,
            'city_Denver': 0,
            'city_Detroit': 0,
            'city_Durham': 0,
            'city_Fort_Worth': 0,
            'city_Fresno': 0,
            'city_Houston': 0,
            'city_Indianapolis': 0,
            'city_Jacksonville': 0,
            'city_Las_Vegas': 0,
            'city_Long_Beach': 0,
            'city_Los_Angeles': 0,
            'city_Louisville': 0,
            'city_Memphis': 0,
            'city_Miami': 0,
            'city_Milwaukee': 0,
            'city_Minneapolis': 0,
            'city_Nashville': 0,
            'city_New_Orleans': 0,
            'city_New_York': 0,
            'city_Oakland': 0,
            'city_Oklahoma_City': 0,
            'city_Omaha': 0,
            'city_Philadelphia': 0,
            'city_Pittsburgh': 0,
            'city_Richmond': 0,
            'city_Sacramento': 0,
            'city_San_Antonio': 0,
            'city_San_Bernardino': 0,
            'city_San_Diego': 0,
            'city_San_Francisco': 0,
            'city_Savannah': 0,
            'city_St._Louis': 0,
            'city_Stockton': 0,
            'city_Tampa': 0,
            'city_Tulsa': 0,
            'city_Washington': 0,
            'state_AL': 0,
            'state_CA': 0,
            'state_CO': 0,
            'state_DC': 0,
            'state_FL': 0,
            'state_GA': 0,
            'state_IL': 0,
            'state_IN': 0,
            'state_KY': 0,
            'state_LA': 0,
            'state_MA': 0,
            'state_MD': 0,
            'state_MI': 0,
            'state_MN': 0,
            'state_MO': 0,
            'state_NC': 0,
            'state_NE': 0,
            'state_NM': 0,
            'state_NV': 0,
            'state_NY': 0,
            'state_OH': 0,
            'state_OK': 0,
            'state_PA': 0,
            'state_TN': 0,
            'state_TX': 0,
            'state_VA': 0,
            'state_WI': 0
            }
        inp["victim_age"] = age
        inp["reported_year"] = year
        inp["POPULATION"] = population
        inp[f"victim_sex_{sex}"] = 1
        inp[f"victim_race_{race}"] = 1
        inp[f"reported_month_{month}"] = 1
        inp[f"reported_weekday_{weekday}"] = 1
        inp[f"season_{season}"] = 1
        inp[f"city_{city}"] = 1
        inp[f"state_{state}"] = 1
        print (inp)

        inp = pd.DataFrame([inp])
        rtn = lgbm_model.predict_proba(inp)[0]
        return rtn
    

