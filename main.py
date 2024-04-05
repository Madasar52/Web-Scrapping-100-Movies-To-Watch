import requests
from bs4 import BeautifulSoup
import smtplib
import os


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3", class_="title")
movie_titles = [title.getText() for title in titles]
movie_titles.reverse()
print(movie_titles)


for movie in movie_titles:
    my_email = os.environ.get("my_email")
    password = os.environ.get("password")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="destination_email",
                            msg=f"Subject: 100 Movies to Watch\n\n{movie}"
                            )




