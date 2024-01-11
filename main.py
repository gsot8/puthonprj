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
@app.route("/rooms/create", methods=["GET", "POST"])
def room_create():
    if request.method == "POST":
        print('here')
        room = Room(
            number=request.json["number"],
            values=request.json["values"],
        )
        print(room)
        app.db.session.add(room)
        app.db.session.commit()
        return 'succses'
    return abort(404)

@app.route("/rooms/book", methods=["GET", "POST"])
def room_create():
    if request.method == "POST":
        print('here')
        timetable = Timetable(

        )
        print(timetable)
        app.db.session.add(timetable)
        app.db.session.commit()
        return 'succses'
    return abort(404)




if __name__ == "__main__":
    app.run()

