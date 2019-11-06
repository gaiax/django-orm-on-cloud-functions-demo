import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import requests
import django

django.setup()

from books.models import Volume

from random import randint


def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    query = request.args.get("query")
    try:
        volumes = get_volumes(query)
    except requests.ConnectionError as e:
        response = {
            "error": {
                "message": "検索に失敗しました。インターネット接続状況を確認してください。"
            }
        }
        return json.dumps(response)
    except Exception as e:
        response = {
            "error": {
                "message": "検索に失敗しました。もう一度試してください。"
            }
        }
        return json.dumps(response)
    else:
        save_volumes(volumes)
        response = {
            "status": "success"
        }
        return json.dumps(response)


def save_volumes(volumes):
    for volume in volumes:
        obj, created = Volume.objects.update_or_create(
            uid=volume["id"],
            defaults={
                "title": volume["volumeInfo"]["title"],
                "publisher": volume["volumeInfo"].get("publisher", "不明"),
                "description": volume["volumeInfo"].get("description", ""),
            },
        )


def get_volumes(query):
    endpoint = "https://www.googleapis.com/books/v1/volumes"
    payload = {"q": query}
    search_response = requests.get(endpoint, params=payload)
    if search_response.ok:
        search_data = search_response.json()
        return search_data["items"]
    else:
        raise Exception("検索に失敗しました。もう一度試してください。")


if __name__ == '__main__':
    result = f()
    print(result)
