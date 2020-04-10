#!/usr/bin/env python3

import requests
import pprint
import json
import dataclasses
from enum import Enum, unique, auto
from bs4 import BeautifulSoup

@unique
class Archetype(Enum):
    NONE = 0
    HERO = 1
    HERALD = 2
    MENTOR = 3
    GUARDIAN = 4
    SHAPESHIFTER = 5
    ALLY = 6
    TRICKSTER = 7
    SHADOW = 8

@unique
class Relation(Enum):
    NONE = 0
    NEUTRAL = 1
    ALLY = 2
    ENEMY = 3

@unique
class RelationType(Enum):
    NONE = 0
    FAMILY = 1
    FRIEND = 2
    NOTFRIEND = 3
    LOVER = 4
    OTHER = 5

@dataclasses.dataclass
class Character:
    movie_id: str
    name: str
    gender: int

@dataclasses.dataclass
class Movie:
    imdb_id: str
    tmdb_id: str
    title: str
    year: str
    duration: str

class EnhancedJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if dataclasses.is_dataclass(o):
                return dataclasses.asdict(o)
            return super().default(o)

def createRelationshipMatrix(charNames: list, movieId: str):
    """Create a csv file that represents the relation between the movie characters

    Args:
        charNames (list): List of characters names of the movie
        movieId (str): Id of the movie in the TMDB
    """
    with open('{}relations/{}_relations.csv'.format(dataDir, movieId), 'w', encoding='utf-8') as relations:
        with open('{}relation_types/{}_relations_types.csv'.format(dataDir, movieId), 'w', encoding='utf-8') as relationsTypes:
                relations.write('chars,{}\n'.format(','.join(charNames)))
                relationsTypes.write('chars,{}\n'.format(','.join(charNames)))
                for name in charNames:
                    relationsTypes.write(name+',\n')
                    relations.write(name+',\n')


def createCharactersInfos(chars: list, movieId: str):
    """Create a csv file that represents all characters with its gender and archetypes

    Args:
        chars (list): A list of chars with its own gender and archetypes
        movieId (str): Id of the movie in the TMDB
    """ 
    with open('{}archetypes/{}_characters.csv'.format(dataDir, movieId), 'w', encoding='utf-8') as csv:
        csv.write('movie_id, character_name, gender, archetype\n')
        
        for char in chars:
            csv.write(char)


dataDir  = '../data/'
prefix = 'https://api.themoviedb.org/3/movie/'
movieIds = ['671', '557', '603', '8587', '11']
castAttr = '/credits'
sufix = '?api_key=fb61737ab2cdee1c07a947778f249e7d&language=en-US'

for movieId in movieIds:
    # Get 
    url = prefix + movieId + castAttr + sufix
    response = requests.get(url).json()['cast'][:60]
    charsDetails = list(map(lambda char: '{},{},{}\n'.format(movieId, 
                                            char['character'], 
                                            char['gender']), response))
    createCharactersInfos(charsDetails, movieId)
    
    charNames = list(map(lambda char: '{}'.format(char['character']), response))
    createRelationshipMatrix(charNames, movieId)