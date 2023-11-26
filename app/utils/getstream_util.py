from stream_chat import StreamChat

from django.conf import settings
from django.utils import timezone

from app.utils.log import log


def create_users(dict_list):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        dict_list = [{**d, "role": "user"} for d in dict_list]
        res = server_client.upsert_users(dict_list)
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "create_user")
            log(f"Cannot create users: {dict_list}", "create_user")
    except:
        log(f"Cannot create users: {dict_list}", "create_user")

# create_users([{"id":"user_id_1"},{"id":"user_id_2"}])


def update_users(dict_list):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        res = server_client.update_users_partial(dict_list)
        if res.status_code() != 200:
            log(f"GetStaream Error: {res}", "update_users")
            log(f"Cannot update users: {dict_list}", "update_users")
    except:
        log(f"Cannot update users: {dict_list}", "update_users")

# update_users([{"id":"user_id_1", "set":{"key_1":"value_1"}},{"id":"user_id_2", "set":{"key_2":"value_2"}}])


def query_users(user_id_list):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        res = server_client.query_users({"id": {"$in": user_id_list}})
        if res.status_code() != 200:
            log(f"GetStaream Error: {res}", "query_users")
            log(f"Cannot query users: {user_id_list}", "query_users")
            return []
        return res.get("users")
    except:
        log(f"Cannot query users: {user_id_list}", "query_users")
        return []

# print(query_users(["user_id_1", "user_id_2"]))


def create_channel(channel_type, channel_id, dict_data, user_id):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        channel = server_client.channel(
            channel_type, channel_id, data=dict_data)
        res = channel.create(user_id)
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "create_channel")
            log(f"Cannot create channel: {channel_id}", "create_channel")
    except:
        log(f"Cannot create channel: {channel_id}", "create_channel")

# create_channel("jobsite", "1234567890", {}, "user_id_1")


def update_channel(channel_type, channel_id, dict_data):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        channel = server_client.channel(channel_type, channel_id)
        res = channel.update_partial(to_set=dict_data)
        if res.status_code() != 200:
            log(f"GetStaream Error: {res}", "update_channel")
            log(f"Cannot update channel: {channel_id}", "update_channel")
    except:
        log(f"Cannot update channel: {channel_id}", "update_channel")

# update_channel("jobsite", "1234567890", {"key_1":"value_1", "key_2":"value_2"})


def query_channels(user_id_list):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        res = server_client.query_channels({"members": {"$in": user_id_list}})
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "query_channels")
            log(f"Cannot query channels: {user_id_list}", "query_channels")
            return []
        return res.get("channels")
    except:
        log(f"Cannot query channels: {user_id_list}", "query_channels")
        return []

# print(query_channels(["user_id_1", "user_id_2"]))


def add_members(channel_type, channel_id, user_id_list):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        channel = server_client.channel(channel_type, channel_id)
        res = channel.add_members(user_id_list)
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "add_member")
            log(f"Cannot add members: {user_id_list}", "add_member")
    except:
        log(f"Cannot add members: {user_id_list}", "add_member")

# add_members("jobsite", "1234567890", ["user_id_1", "user_id_2"])


def remove_members(channel_type, channel_id, user_id_list):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        channel = server_client.channel(channel_type, channel_id)
        res = channel.remove_members(user_id_list)
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "remove_members")
            log(f"Cannot remove members: {user_id_list}", "remove_members")
    except:
        log(f"Cannot remove members: {user_id_list}", "remove_members")

# remove_members("jobsite", "1234567890", ["user_id_1", "user_id_2"])


def query_members(channel_type, channel_id, user_id_list):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        channel = server_client.channel(channel_type, channel_id)
        res = channel.query_members(
            filter_conditions={"id": {"$in": user_id_list}})
        return res
    except:
        log(f"Cannot query members: {user_id_list}", "query_members")
        return []

# print(query_members("jobsite", "1234567890", ["user_id_1", "user_id_2"]))


def send_message(channel_type, channel_id, context, user_id):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        channel = server_client.channel(channel_type, channel_id)
        res = channel.send_message(context, user_id)
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "send_message")
            log(f"Cannot send message: {user_id}", "send_message")
    except:
        log(f"Cannot send message: {user_id}", "send_message")

# send_message("jobsite", "1234567890", {"text":"text"}, "user_id_1")


def update_message(message_id, context, user_id):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        res = server_client.update_message_partial(
            message_id, {"set": context}, user_id)
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "update_message")
            log(f"Cannot update message: {user_id}", "update_message")
    except:
        log(f"Cannot update message: {user_id}", "update_message")

# update_message("753b66cd-5fcc-4702-8bb7-335cb154945a", {"key_1":"value_1"}, "user_id_1")


def send_channel_event(channel_type, channel_id, context, user_id):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        channel = server_client.channel(channel_type, channel_id)
        res = channel.send_event(context, user_id)
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "send_channel_event")
            log(f"Cannot send channel event: {user_id}", "send_channel_event")
    except:
        log(f"Cannot send channel event: {user_id}", "send_channel_event")

# send_channel_event("jobsite", "1234567890", {"type":"type","text":"text"}, "user_id_1")


def send_user_event(user_id, context):
    try:
        server_client = StreamChat(
            api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        res = server_client.send_user_custom_event(user_id, context)
        if res.status_code() != 201:
            log(f"GetStaream Error: {res}", "send_user_event")
            log(f"Cannot send user event: {user_id}", "send_user_event")
    except:
        log(f"Cannot send user event: {user_id}", "send_user_event")

# send_user_event("user_id_1", {"type":"type","text":"text"})


def create_token(user_id):
    try:
        server_client = StreamChat(api_key=settings.GETSTREAM_API_KEY, api_secret=settings.GETSTREAM_API_SECRET)
        res = server_client.create_token(user_id, exp=timezone.datetime.utcnow() + timezone.timedelta(days=365))
        return res
    except:
        log(f"Cannot create token: {user_id}", "create_token")
        return None

# print(create_token("user_id_1"))
