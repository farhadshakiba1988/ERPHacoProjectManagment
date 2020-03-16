import os
from distutils.command.build import build
import httplib2
from datetime import datetime
import arrow
from django.http import HttpResponseRedirect
from django.conf import settings
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from hacoERdb.models import CredentialsModel

client_id = settings.GP_CLIENT_ID
client_secret = settings.GP_CLIENT_SECRET

CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '..', 'client_secret.json')

FLOW = flow_from_clientsecrets(
    redirect_uri=settings.GOOGLE_OAUTH2_REDIRECT)


def get_service(request):
    storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY, request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url), False
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        service = build("calendar", "v3", http=http)
    return service, True


def get_calendar_events_list(request):
    if not request.user.is_authenticated:
        return []
    service, is_connected = get_service(request)
    if not is_connected:
        return []
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()

        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
    request = service.events().list(calendarId='primary')
    user_events = []
    while request is not None:
        response = request.execute()

        for event in response.get('items', []):
            each = {}
            each['id'] = event['id']
            each['description'] = event.get('description', '')
            each['summary'] = event.get('summary', '')
            each['htmlLink'] = event.get('htmlLink', '')

            date_format = "%Y-%m-%d %H:%M:%S"
            if 'start' in event.keys():
                if 'dateTime' in event['start'].keys():
                    start_date = arrow.get(event['start']['dateTime']).format('YYYY-MM-DD HH:mm:ss')
                    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
                    published_date = datetime.strptime(start_date, date_format)
                    each['start_date'] = published_date.date()
                elif 'date' in event['start'].keys():
                    each['start_date'] = event['start']['date']
            if 'end' in event.keys():
                if 'dateTime' in event['end'].keys():
                    start_date = arrow.get(event['end']['dateTime']).format('YYYY-MM-DD HH:mm:ss')
                    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
                    published_date = datetime.strptime(start_date, date_format)
                    each['end_date'] = published_date.date()
                elif 'date' in event['end'].keys():
                    each['end_date'] = event['end']['date']
            user_events.append(each)

        request = service.events().list_next(request, response)
    return user_events


def delete_google_calendar_event(request, event_id):
    service, is_connected = get_service(request)
    if not is_connected:
        return False
    try:
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        return True
    except:
        return False


def create_google_calendar_event(request, user, summary):
    service, is_connected = get_service(request)
    if not is_connected:
        return service, 'redirect'
    try:
        event = service.events().insert(calendarId=request.user.email, body=summary).execute()
        # print event
        return event, True
    except:
        return '', False
