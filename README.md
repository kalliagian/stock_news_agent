# Stock news Agent

In order to run the application as a docker container, run the following commands:

```bash
docker build -t news-agent-app .
docker run -p 5000:5000 -d --name news-agent-app news-agent-app
```

After a few of seconds (may take up to a few minutes) the app is up and running. Visit localhost:5000 to visit the UI.
