from flask import Blueprint, Flask, render_template, redirect, request

import repositories.print_repository as print_repository 
import repositories.artist_repository as artist_repository

from models.artist import Artist

artists_blueprint = Blueprint("artists", __name__)

@artists_blueprint.route("/artists")
def display_artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", all_artists = artists)

@artists_blueprint.route("/artists/new", methods=['GET'])
def new_artist():
    return render_template("artists/new.html")

@artists_blueprint.route("/artists", methods=['POST'])
def create_new_artist(): 
    name = request.form["name"]
    image_pathway = request.form["image_pathway"]
    artist = Artist(name, image_pathway)
    artist_repository.save(artist)
    return redirect("/artists")

@artists_blueprint.route("/artists/<id>")
def filter(id):
    artist = artist_repository.select(id)
    prints = artist_repository.prints(artist)
    return render_template("artists/filter.html", artist=artist, prints=prints)

@artists_blueprint.route("/artists/<id>/delete", methods=["POST"])
def delete_artist(id):
    artist_repository.delete(id)
    return redirect("/artists")

@artists_blueprint.route("/artists/<id>/edit", methods=["GET"])
def edit_artist(id):
    artist = artist_repository.select(id)
    return render_template("artists/edit.html", artist=artist)

@artists_blueprint.route("/artists/<id>", methods=['POST'])
def update_artist(id):
    name = request.form["name"]
    image_pathway = request.form["image_pathway"]
    artist = Artist(name, image_pathway, id)
    artist_repository.update(artist)
    return redirect("/artists")