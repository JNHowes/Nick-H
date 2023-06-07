# Author: Nick Howes
# GitHub username: JNHowes
# Date:June 07, 2023
# Description:  Defines classes to manage movies, streaming services, and a streaming guide, allowing users to add,
# delete, and search for movies available on different streaming services.

class Movie:
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre

    def get_director(self):
        return self._director

    def get_year(self):
        return self._year


class StreamingService:
    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie):
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, movie_title):
        if movie_title in self._catalog:
            del self._catalog[movie_title]


class StreamingGuide:
    def __init__(self):
        self._streaming_services = []

    def add_streaming_service(self, streaming_service):
        self._streaming_services.append(streaming_service)

    def delete_streaming_service(self, name):
        for streaming_service in self._streaming_services:
            if streaming_service.get_name() == name:
                self._streaming_services.remove(streaming_service)
                break

    def where_to_watch(self, movie_title):
        for streaming_service in self._streaming_services:
            catalog = streaming_service.get_catalog()
            if movie_title in catalog:
                movie = catalog[movie_title]
                result = [f"{movie.get_title()} ({movie.get_year()})"]
                result.extend([service.get_name() for service in catalog.values()])
                return result
        return None
