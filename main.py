from init import create_app
import requests
from flask import request,redirect,url_for,render_template,abort
from tables import User,Room,Timetable

app = create_app()

@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        print('here')
        user = User(
            login=request.json["login"],
            surname=request.json["login"],
        )
        print(user)
        app.db.session.add(user)
        app.db.session.commit()
        return 'succses'
    return abort(404)


if __name__ == "__main__":
    app.run()

