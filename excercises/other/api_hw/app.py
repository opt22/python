from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__) 
                                                                                   
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

class GuideSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'title', 'content')

guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)

#Endpoint to create new guide
@app.route('/guide', methods=["POST"])
def add_guide():
    title= request.json['title']
    content = request.json['content']
    new_guide = Guide(title, content)
    db.session.add(new_guide)
    db.session.commit()
    guide = Guide.query.get(new_guide.id)
    return guide_schema.jsonofy(guide)

#endpoint to query all guides
@app.route("/guides", methods=["GET"])
def get_guides():
    all_guides = Guide.query.all()
    result = guides_schema.dump(all_guides)
    return jsonify(result)

#endpoint to query a single guide
@app.route("/guide/<id>", methods=["GET"])
def get_guide(id):
    guide = Guide.query.get(id)
    return guide_schema.jsonify(guide)

#endpoint to query and update single guide
@app.route("/guide/<id>", methods=["PUT"])
def guide_update(id):
    guide=Guide.query.get(id)
    title=request.json['title']
    content=request.json['content']
    guide.title = title
    guide.content=content
    db.session.comit()
    return guide_schema.jsonify(guide)

#endpoint to delete single record

@app.route("/guide/<id>", methods=["DEL"])
def guide_delete(id):
    guide = Guide.query.get(id)
    db.session.delete(guide)
    db.session.commit()
    return guide_schema.jsonify(guide)

if __name__ == '__main__':
    app.run(debug=True)
