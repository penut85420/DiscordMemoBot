import datetime as dt

def ParseDatetime(inn: str):
    try:
        now = dt.datetime.utcnow()
        t = dt.datetime.strptime(f'{now.year}{inn}', "%Y%m%d%H%M")
        return t
    except Exception as e:
        print(e)
        return None
