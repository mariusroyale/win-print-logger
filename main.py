import sys
import time
import click
import win32evtlogutil
import win32evtlog


@click.command()
@click.option("-a", "--app_name", default='', help="App Name", show_default=True)
@click.option("-e", "--event_id", default='', help="Event ID", show_default=True)
@click.option("-c", "--category", default='', help="Event Category", show_default=True)
@click.option("-s", "--event_string", default='', help="Event String", show_default=True)
@click.option("-d", "--event_data", default='', help="Event Data", show_default=True)
def main(app_name, event_id, category, event_string, event_data):
    print("Python {0:s} on {1:s}".format(sys.version, sys.platform))

    DUMMY_EVT_APP_NAME = app_name
    DUMMY_EVT_ID = int(event_id)  # Got this from another event
    DUMMY_EVT_CATEG = int(category)
    DUMMY_EVT_STRS = [event_string]
    DUMMY_EVT_DATA = bytes(event_data, 'utf-8')  # b"Dummy event data"

    print("Current time: {0:s}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    win32evtlogutil.ReportEvent(
        DUMMY_EVT_APP_NAME, DUMMY_EVT_ID, eventCategory=DUMMY_EVT_CATEG,
        eventType=win32evtlog.EVENTLOG_WARNING_TYPE, strings=DUMMY_EVT_STRS,
        data=DUMMY_EVT_DATA)


if __name__ == '__main__':
    main()
