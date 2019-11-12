# Local Imports
from Models.movie import Movie
from Models.people import People
from Models.company import Company
from PeopleFactory import PeopleFactory
from RoleFactory import RoleFactory
from MovieFactory import MovieFactory
from CompanyFactory import CompanyFactory


class Factory:

    # Mega Function
    @staticmethod
    def insert_all(movie_data):
        movie = Movie(movie_data["movie"])
        cast = movie_data["cast"]
        crew = movie_data["crew"]
        companies = movie_data["companies"]

        # @return movie_id
        movie_id = MovieFactory.insert(movie)

        # @return cast_ids
        cast_ids = []
        for actor in cast:
            actor = People(actor)
            actor = (PeopleFactory.insert(actor),
                     RoleFactory.insert("Actor"))
            cast_ids.append(actor)

        # @retun crew_ids
        crew_ids = []
        for person in crew:
            technician = People(person)
            technician = (PeopleFactory.insert(technician),
                          RoleFactory.insert(person["role"]))
            crew_ids.append(technician)

        # @return companies_ids
        companies_ids = []
        for stuff in companies:
            company = Company(stuff)
            company = (CompanyFactory.insert(company),
                       RoleFactory.insert("production"))
            companies_ids.append(company)

        for actor in cast_ids:
            RoleFactory.insert_mpr(actor, movie_id)

        for crew in crew_ids:
            RoleFactory.insert_mpr(crew, movie_id)

        for company in companies_ids:
            RoleFactory.insert_mcr(company, movie_id)
