from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Atributos de Cards: (card id, expiration month, expiration year, name on card, user id)

class CardsDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertCard(self, expirationMonth, expirationYear, nameOnCard, userid):
        cursor = self.conn.cursor()
        query = "insert into cards(expirationmonth,expirationyear,nameoncard,userid) values(%i,%i,%s,%i));"
        cursor.execute(query, ([expirationMonth], [expirationYear], nameOnCard, [userid]))
        cardid = cursor.fetchone()[0]
        self.conn.commit()
        return cardid