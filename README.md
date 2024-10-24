# movie-recommendation-app
This app is a very basic movie recommendation system. The user selects a movie from the dropdown and the app recommends 5 movies based on their similarity.

### Please view the following video for source code:
https://www.youtube.com/watch?v=kuC38ZCcbZI

### The corresponding github page is as follows:
https://github.com/Chando0185/movie_recommender_system

### Dataset from Kaggle:
https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k

### API Key from TMDB:
https://developer.themoviedb.org/docs/getting-started

# How to Use/Modify
![sample_output](https://github.com/user-attachments/assets/1cc091a1-5c3f-4902-99f5-ef1993f5a564)

## Installation & Setup
### Setup
* Download the files provided into a folder of your choice (example folder title: "movie-recommendation-app")
* Open the folder with VSCode or similar code editing program
* Go to [TMDB](https://developer.themoviedb.org/docs/getting-started), create an account and generate an API key
* Create a new file called "api.py" inside the folder
* Open the api.py and create a variable called "api_key" and set your new variable equal to your api key from TMDB
* Should be as follows:
```
api_key= "(YOUR KEY HERE)"
```
* Open "main.ipynb" and run all
* (This creates the files "movie_list.pkl" and "similarity.pkl" for your local machine)
* Open  a terminal window and navigate to the folder you created (called "movie-recommendation-app")
* Use the command "streamlit run app.py" to run streamlit
* A new browser window should appear that allows you to interact with the app
* You should be seeing the following:
* ![sample_output](https://github.com/user-attachments/assets/1cc091a1-5c3f-4902-99f5-ef1993f5a564)
* Select a movie from the dropdown and the app will generate your recommendations!

### To Modify
Using VSCode or a similar program, change whatever you like! 

For reference, this app was written in Python using streamlit, Jupyter Notebook, pandas, and pickle. It fetches movie posters from TMDB using an API Key.


