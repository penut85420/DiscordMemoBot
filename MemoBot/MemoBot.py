import datetime as dt

class MemoData:
    TIMEZONE = dt.timedelta(hours=8)

    def __init__(self, channel, author, timestamp, content) -> None:
        self.Channel = channel
        self.Author = author
        self.Timestamp = timestamp
        self.Content = content

    def check(self):
        now = dt.datetime.utcnow() + MemoData.TIMEZONE
        if self.Timestamp < now:
            return True
        return False

class MemoBot:
    def __init__(self):
        self.database = list()

    def add(self, data: MemoData):
        self.database.append(data)

    def check(self) -> MemoData:
        for d in self.database:
            if d.check():
                yield d

    def show(self):
        print(self.database)

    def save(self):
        # TODO: Parse Memo Data And Save As JSON Data
        pass

    def load(self):
        # TODO: Load JSON Data And Parse Into Object
        pass
