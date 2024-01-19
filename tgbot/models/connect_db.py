import pymysql.cursors

from tgbot.config import load_config


class Base:
    """Connect to database and execute query"""
    __slots__ = {"config", "connection", "id"}

    def __init__(self, id: int = 0):
        self.id = id
        self.config = load_config(".env")
        self.connection = pymysql.connect(
            host=self.config.db.host,
            port=3306,
            user=self.config.db.user,
            password=self.config.db.password,
            database=self.config.db.database,
            autocommit=True,
            # cursorclass=pymysql.cursors.DictCursor
        )


class NewUser(Base):
    def add_user(self, username=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS(SELECT user_id FROM users WHERE user_id = {user_id})".format(user_id=self.id))
                res = cursor.fetchone()
                if res[0] == False:
                    cursor.execute(
                        "INSERT INTO users(user_id, username) VALUES ({user_id}, '{username}')".format(user_id=self.id, username=username))
                    return True
                else:
                    return False
        except:
            print("Error in add_user")
        finally:
            self.connection.close()


class Filter(Base):
    def filter_admin(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT EXISTS(SELECT useradmin FROM users WHERE user_id = {user_id} and useradmin = True)".format(user_id=self.id))
                res = cursor.fetchone()
                if res[0] == True:
                    return True
                else:
                    return False
        except:
            print("Error in filter_admin")

        finally:
            self.connection.close()


