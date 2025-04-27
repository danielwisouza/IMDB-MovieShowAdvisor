# Movie-Show Advisor: IMDB Streaming Data Analysis 🎥

## Table of Contents
1. [Introduction](#1-introduction)
2. [Technologies Used](#2-technologies-used)
3. [Questions Analyzed](#3-questions-analyzed)
4. [Data Source](#4-data-source)
5. [Key Insights](#5-key-insights)
6. [Setup and Installation](#6-setup-and-installation)

## 1. Introduction

This project is designed to analyze IMDB movie and TV series data. We will explore various aspects of movie data such as genres, ratings, and the relationship between movie duration and genres. By analyzing the data, we aim to answer the following questions:

### Questions Analyzed:
- **Question 1**: What are the most common movie categories on IMDB?
- **Question 2**: How many titles are there per genre?
- **Question 3**: What is the median rating of movies by genre?
- **Question 4**: What is the median rating of movies based on their release year?
- **Question 5**: How many movies are rated by genre and release year?
- **Question 6**: Which movie has the longest duration? Calculate the percentiles.
- **Question 7**: What is the relationship between movie duration and genre?
- **Question 8**: How many movies are produced per country?
- **Question 9**: What are the top 10 best-rated movies?
- **Question 10**: What are the top 10 worst-rated movies?

## 2. Technologies Used

This application was developed using the following technologies:

- **Python**
- **SQL**
- **Google Colab Cloud Environment**: [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb?hl=pt-BR)

The project uses Python libraries like `pandas`, `numpy`, and `sklearn` to perform data analysis and machine learning tasks.

## 3. Questions Analyzed

The project analyzes a set of questions related to IMDB movie data. These questions help to understand trends, relationships, and the distribution of data such as movie genres, ratings, and other factors. You can check the questions listed in the introduction section above.

## 4. Data Source

The data for this project was sourced from IMDB:

- **IMDB**: [IMDB Website](https://www.imdb.com/)

This dataset contains information about movies and TV series, including their ratings, genres, and release years.

## 5. Key Insights

After analyzing the IMDB data, we uncover key insights that answer the above questions, helping to guide recommendations for users of streaming platforms. For example:
- Understanding which genres are most common and their ratings.
- Analyzing the relationship between a movie's duration and its genre.
- Identifying the best and worst-rated movies.

## 6. Setup and Installation

To run this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd Movie-Show-Advisor
    ```

2. Install necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the analysis in Google Colab or locally by executing the main Python script:
    ```bash
    python main.py
    ```

4. For detailed steps on data preparation and model execution, refer to the `README.md` file within the repository.
