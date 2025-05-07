# Stock news Agent

### Setup instructions

In order to run the application as a docker container, run the following commands:

```bash
docker build -t news-agent-app .
docker run -p 5000:5000 -d --name news-agent-app news-agent-app
```

After a few of seconds (may take up to a few minutes) the app is up and running. Visit localhost:5000 to visit the UI.


### Project Structure
* agent.py - Contains the NewsSummarizationAgent class used for retrieving and summarizing news articles.
* main.py - Taipy-based UI application for interacting with the agent and viewing summaries.
* news_dataset/2020_processed.json - News dataset used by the agent.
* colab_notebooks/ - Contains notebooks for dataset creation, fine-tuning and evaluation (can also be opened directly in Colab using the links below).


### Colab Notebooks

The following Colab notebooks were used:
* Dataset creation: https://colab.research.google.com/drive/1x5-HdyjD2Z1Rjp_ho041xamItjKQUYRn?usp=sharing
* Model fine-tuning: https://colab.research.google.com/drive/1UMEOUoVOJoCLV3dS1Naq3u4VEPu3NRJZ?usp=sharing
* Evaluation: https://colab.research.google.com/drive/1wrsLKXy8h95YVoMxsBnGUHmNCiSJFIbH?usp=sharing