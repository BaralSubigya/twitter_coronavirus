# Coronavirus Twitter MapReduce Analysis

## Project Overview
This project analyzes 1.1 billion geotagged tweets from 2020 to study how discussion of COVID-19 spread across languages, countries, and time. Because the dataset is too large for traditional analysis, I implemented a parallel MapReduce pipeline in Python and Bash on a multi-processor server.

The mapper scans each day of tweets and extracts hashtag usage by both language and country. The reducer aggregates the daily outputs into global statistics. Finally, visualization scripts generate interpretable plots.

## Results

### English hashtag (#coronavirus)
![Top languages](plots/lang_coronavirus.png)
![Top countries](plots/country_coronavirus.png)

### Korean hashtag (#코로나바이러스)
![Top languages](plots/lang_korean_hashtag.png)
![Top countries](plots/country_korean_hashtag.png)

### Hashtag usage over time
![Time series](plots/hashtag_timeseries.png)

## Key Findings
The English hashtag appears globally across many languages, while the Korean hashtag is overwhelmingly used in Korean tweets.

Country plots show Korean hashtag usage concentrated in South Korea, while English usage is globally distributed.

Hashtag usage spikes sharply during early 2020 and declines afterward, matching real-world pandemic awareness.
