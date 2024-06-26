from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from passlib.hash import sha256_crypt

from src.project_enums import SearchTypes, ObjectTypes

from src.Data.object_factory import ObjectFactory
from src.Data.search_manager import SearchManager
from src.api.query_parser import QueryParser


app = Flask(__name__)
auth = HTTPBasicAuth()

query_parser = QueryParser()
search_manager = SearchManager()
object_factory = ObjectFactory()


@app.get("/cereal")
def cereal_get():
    query_fields = query_parser.parse(request.args)

    cereals = search_manager.search(SearchTypes.CEREAL, fields=query_fields)

    if len(cereals) == 1:
        cereals = cereals[0]

    cereals = [cereal.to_dict() for cereal in cereals]

    return jsonify(cereals), 200


# @authenticate_decorator
@app.post("/cereal")
@auth.login_required
def cereal_post():
    if not request.is_json:
        return {"error": "Request must be JSON"}, 415

    post_data = request.get_json()

    if 'id' in post_data:
        post_id = post_data['id']
        fields = query_parser.parse({'id': post_id})

        cereals = search_manager.search(SearchTypes.CEREAL, fields=fields)

        if cereals and len(cereals) == 1:
            return _cereal_update(post_data, cereals[0])
        elif cereals:
            return {"error": f"Found multiple cereals with id = {post_id}"}, 500
        else:
            return {"error": "You can't decide the ID yourself"}, 400
    else:
        return _cereal_post(post_data)


def _cereal_post(post_data):
    cereal = object_factory.build(ObjectTypes.CEREAL, **post_data)
    cereal.add()

    return jsonify(cereal.to_dict()), 200


def _cereal_update(post_data, cereal):
    cereal_dictionary = cereal.to_dict()

    for key, value in post_data.items():
        cereal_dictionary[key] = value

    cereal = object_factory.build(ObjectTypes.CEREAL, **cereal_dictionary)

    cereal.update()

    return jsonify(cereal.to_dict()), 200


# @authenticate_decorator
@app.delete("/cereal")
@auth.login_required
def cereal_delete():
    if not request.is_json:
        return {"error": "Request must be JSON"}, 415

    post_data = request.get_json()

    if 'id' not in post_data:
        return {"error": "Deletion requires an ID"}, 400

    post_id = post_data['id']
    fields = query_parser.parse({'id': post_id})

    cereals = search_manager.search(SearchTypes.CEREAL, fields=fields)

    if cereals and len(cereals) == 1:
        cereal = cereals[0]
        cereal.remove()
        return jsonify(cereal.to_dict()), 200
    elif cereals:
        return {"error": f"Found multiple cereals with id = {post_id}"}, 500
    else:
        return {"error": f"A cereal with {post_id} doesn't exist"}, 400


@app.get("/logo")
def logo_get():
    raise NotImplementedError


@auth.verify_password
def verify_password(username, password):
    print(f'inbuilt - {username}: {password}')
    fields = query_parser.parse({'name': username})

    users = search_manager.search(SearchTypes.USER, fields=fields)

    if len(users) != 1:
        return False

    user = users[0]

    verified = sha256_crypt.verify(password, user.password)
    if username == user.name and verified:
        return user

    return False


def run():
    app.run(debug=True, port=80)
    print()
    # app.run(debug=True, port=80, ssl_context='adhoc')


if __name__ == '__main__':
    app.run(debug=True, port=80)
    # app.run(debug=True, port=80, ssl_context='adhoc')
