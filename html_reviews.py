from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

html = ''
ratings = []
dates = []

# with open('src.html', encoding='UTF-8') as f:
#     html = f.read()
# #
# root1 = BeautifulSoup(html, features='html.parser')
# reviews_page = root1.findAll(attrs= {'class':'business-reviews-card-view__review'})
#
# for i in range(len(reviews_page)):
#     r = reviews_page[i]
#     file = open(f'file{i}.html', 'w', encoding='UTF-8')
#     file.write(str(r))
#
#     print()

for i in range(11):
    with open(f'file{i}.html', encoding='UTF-8') as file:
        html = file.read()

    root = BeautifulSoup(html, features='html.parser')
    rating = root.find_all(attrs={'class':'business-rating-badge-view__star _size_m'})
    data = root.find(attrs={'class':'business-review-view__date'}).text
    ratings.append(len(rating))
    dates.append(data)

ratigs = np.array(ratings)
dates = np.array(dates)

plt.plot(dates, ratigs)
plt.show()
print(ratigs, dates)