import datetime


def current_ist_time() -> str:
    date = datetime.datetime.now()
    istTZDelta = datetime.timedelta(hours=5, minutes=30)
    istTZObject = datetime.timezone(istTZDelta, name='IST')
    return date.astimezone(istTZObject).strftime("%d-%b-%Y %I:%M:%S%p")
