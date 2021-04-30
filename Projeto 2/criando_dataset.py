
import pandas as pd
import random
import numpy as np
import json
from itertools import permutations, cycle
from pandas.core.algorithms import unique
from pandas.core.frame import DataFrame
from faker import Faker
# -*- coding: utf-8 -*-


def createEmail(how_many, faker=Faker()):
    email = []
    for i in range(0, how_many):
        email.append(faker.email())
    return email


def createClass(how_many, faker=Faker()):
    classics = []
    for i in range(0, how_many):
        classics.append(random.randint(0, 5))
    return classics


def createTitles(how_many, faker=Faker()):
    filmes = ["Filme1", "Filme2", "F3", "F$", "f8a"]
    titles = []
    for i in range(0, how_many):
        titles.append(getRandomFilms())
    return titles


def getRandomFilms():
    file = open("./Datasets/movie.json")
    data = json.load(file)
    file.close()
    return data[random.randint(0, 1000)]['name']


def uniteLists(film, clas):
    result = []
    for i in range(0, len(film)):
        unite = {random.choice(random.sample(
            film, len(film))): random.choice(clas)}
        result.append(unite)
    return result


def insertData(email, film, cla, data=pd.DataFrame()):
    try:
        dic = [{
            "Email": email,
            "Filmes": [{film: cla}]
        }]
        data.append(dic)
        return "SUCESS"
    except:
        return "FAIL"


def filmsUser(email, films):
    films_from_user = []
    for i in films:
        films_from_user.append(i)
    return films_from_user


def clasUser(films, clas):
    clas_list = []
    for i in films:
        randomized_class = random.choice(clas)
        class_film = {i: randomized_class}
        clas_list.append(randomized_class)
    return clas_list

def datasStyle(data_type,email_data, films, clas):
    list_films = filmsUser(email_data, films)
    list_clas = clasUser(films,clas)
    if(data_type =="film"):
        data = {'Filme   ': {
        '': {"": list_films[0]}}}
        df = pd.DataFrame.from_dict(pd.json_normalize(data))
        return df
    elif(data_type =="clas"):
        data = {'Classificação   ': {
        '': {"": list_clas[0]}}}
        df = pd.DataFrame.from_dict(pd.json_normalize(data))
        return df
    else: 
        return None

def insertUserfilm(email, film, clas, data):
    data_list = []
    series = pd.Series([email,film[0], clas[0]], index=["Email.", "Filmes","Classificação"])
    data_list.append(series)
    for i in range(1,len(film)):
        series = pd.Series([email,film[i], clas[i]], index=["Email.", "Filmes","Classificação"])
        data_list.append(series)
    return data_list

def unionDatas(email_data, films, clas):
    randomized_email = email_data[random.randint(0, 10)]
    data_film = datasStyle("film",email_data,films,clas)
    data_clas = datasStyle("clas",email_data,films,clas)
    list_films = filmsUser(email_data, films)
    list_clas = clasUser(films,clas)
    null_data = {"":['']}
    data_pd = pd.DataFrame(pd.json_normalize(null_data, meta_prefix=True, record_prefix=' '))
    pd.set_option('display.max_colwidth', 50)
    data_pd.insert(0,"Email", randomized_email)
    data_pd.insert(1,"Filmes",data_film)
    data_pd.insert(2,"Classificação",data_clas)
    df = pd.DataFrame(insertUserfilm(randomized_email,list_films, list_clas,data_pd))
    return df

'''
def correctJSON():
    file=open("./Datasets/dataAna.json", "r")
    file_json=json.load(file)
    df=pd.io.json.json_normalize(file_json)
    print(df)
    file.close()
'''
def concatDatasets(how_many_datasets,email_data,film_data,clas_data):
    data_concat = None
    for i in range(0, how_many_datasets):
        data = unionDatas(email_data,film_data,clas_data)
        data_concat = pd.concat([data,data_concat], ignore_index=True)
    return data_concat

def exportDatas(data_to_export):
    data_to_export.to_json('./Datasets/DatasetMovies.json', orient='records', lines=False, force_ascii=False, indent=4)



def openData():
    f=open("./Datasets/DatasetMovies.json", "r")
    file_json=pd.read_json(f, orient = 'columns')
    f.close()
    return file_json


def initialization():
    email_data = createEmail(10)
    film_data = createTitles(10)
    clas_data = createClass(10)
    result = concatDatasets(3,email_data,film_data,clas_data)
    exportDatas(result)


if __name__ == "__main__":
    initialization()
