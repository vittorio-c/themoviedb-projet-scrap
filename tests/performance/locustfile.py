from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    url = "http://localhost:5000"
    homepage = url + "/"
    movies = "/movies?page=1"

    @task
    def home_test(self):
        self.client.get(self.homepage)

    @task
    def movies_test(self):
        self.client.get(self.movies)
