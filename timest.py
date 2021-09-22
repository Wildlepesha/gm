import sqlite3
import time
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np
import datetime
import seaborn as sns

conn = sqlite3.connect('dates_and_ratings.db')
cur = conn.cursor()

unique_dates = set()
neg_ratings = []
pos_dates = []
pos_ratings = []
neg_dates = []

plt.style.use('seaborn')

c = 0
cur.execute("SELECT * FROM reviews")
data = cur.fetchall()
cur.execute("CREATE TABLE IF NOT EXISTS results (rating, timestamp)")


def insert_data(data):
    for i in data:
        unique_dates.add(i[1])
        date_to_ts = datetime.strptime(str(i[1]), "%d.%m.%Y")
        date_to_ts = time.mktime(date_to_ts.timetuple())
        cur.execute("INSERT INTO results VALUES (?, ?)", (i[0], date_to_ts))
    conn.commit()


# insert_data(data)

cur.execute("SELECT timestamp, sum(rating) AS 'Total ratings' FROM results WHERE rating <= 2 GROUP BY timestamp")
neg_data = cur.fetchall()
cur.execute("SELECT timestamp, sum(rating) AS 'Total ratings' FROM results WHERE rating > 2 GROUP BY timestamp")
pos_data = cur.fetchall()

for i in neg_data:
    neg_ratings.append(i[1])
    neg_dates.append(datetime.datetime.fromtimestamp(i[0]))

for i in pos_data:
    pos_ratings.append(i[1])
    pos_dates.append(datetime.datetime.fromtimestamp(i[0]))


neg_ratings = np.array(neg_ratings)
neg_dates = np.array(neg_dates)
pos_dates = np.array(pos_dates)
pos_ratings = np.array(pos_ratings)
plt.plot_date(neg_dates, neg_ratings, linestyle='solid')
# plt.plot_date(pos_dates, pos_ratings, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.show()