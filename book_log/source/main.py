import pandas as pd

class BookDB:
    def __init__(self):
        self._bookdf = pd.DataFrame(
            {
                'title': [],
                'author': [],
                'country': []
            }
        )

    def add_book(self, title, author, country):
        self._bookdf.loc[len(self._bookdf)] = {
            'title': title,
            'author': author,
            'country': country
        }

    def get_dataframe(self):
        return self._bookdf


bookdb = BookDB()
bookdb.add_book('Sherlock Holmes', 'Arthur Connan Doyle', 'England')

bdf = bookdb.get_dataframe()
bdf.to_json(r'C:\Users\Gamer\Documents\Python\projetos básicos\book_log\database\bookdb.json')
print(bdf)
