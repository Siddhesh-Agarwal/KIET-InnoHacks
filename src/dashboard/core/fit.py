# use google fit API to fetch data about:
# Blood pressure, glucose level, heart beat, step tracker, sleep tracker, hydration data

# Import libraries
from requests import Response, get, api_view
import json
import pickle
from os import path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# Get credentials
SCOPES = ["https://www.googleapis.com/auth/fitness.activity.read"]
SERVICE_ACCOUNT_FILE = "api-project-248165331787-5a2b3821f120.json"


def main():
    credentials = None
    if path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_console()
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

    fit = build("fitness", "v1", credentials=credentials)

    # Call the Drive v3 API
    response = fit.users().dataSources().list(userId="me").execute()
    datasources = response.get("dataSource", [])
    for datasource in datasources:
        if "blood_pressure" in datasource["dataStreamId"]:
            print("Blood pressure:")
            print(datasource)
            break
    return datasource


@api_view(["GET"])
def googleFitView(request):
    social_token = SocialToken.objects.get(account__user=2)
    token = social_token.token

    url_session = "https://fitness.googleapis.com/fitness/v1/users/me/sessions"

    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    session_call = get(url_session, headers=headers)

    return Response(session_call)
