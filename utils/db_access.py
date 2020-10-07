import pymysql.cursors
import json
from models.Website import Website


def as_website(dct):
    return Website(dct.get('name'), dct.get('command_url'))

class db_access:


    @staticmethod
    def get_records():
        connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='Alexandre123',
                                         db='Voicee',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `Websites`"
                cursor.execute(sql)
                result = cursor.fetchall()
                json_data = json.dumps(result, indent=4, sort_keys=True, default=str)
                parsedJson = json.loads(json_data, object_hook=as_website)
                return parsedJson
        finally:
            connection.close()