import vk_api
from config import my_token


session = vk_api.VkApi(token=my_token)
vk = session.get_api()


def get_user_status(user_id):
    status = session.method("status.get",{"user_id": user_id})
    print(status["text"])

def set_user_status():
    vk.status.set(text="bot лишит тебя забот")


def searh_users_vk():
    danie_vk = vk.users.search(count=200, city=56, sex=1, age_from=25, age_to=45)
    print("function work")
    print(danie_vk)

searh_users_vk()

# set_user_status()