# Interview-site challenge

## Starting the service locally
### Docker
```
docker build -t webapp . && docker run -p 8080:8080 webapp
```

**OR**

### Docker Compose
```
docker-compose up
```

**OR**

### Python bare metal
```
python3 -m venv venv && source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

**All of options for running will result in the web app running on localhost:8080**

## Scenario

**Given** I am at the home page of the site

**When** I search for iPhone

**Then** I am taken to the results page

**And** every result in the results page has a price greater than £0.00

## Challenge
- Write a test and framework that will automatically verify the Scenario described above
- Consider framework maintainability
- You have 90 minutes
