from database.db import users_col


def get_user(telegram_id):
    return users_col.find_one({
     "telegraam_id":telegram_id
    })

def save_user(user):
    users_col.update_one(
        {"telegram_id":user.telegram_id},
        {"$set":user.__dict__},
        upsert=True
    )
