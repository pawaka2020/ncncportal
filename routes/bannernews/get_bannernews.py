# routes/bannernews/get_bannernews.py
import justpy as jp
from models.mongodb.db import db
from models.mongodb.fullnews import FullNews

def get_bannernews():
    bannernews_list = list(db['bannernews'].find({}))

    result = [{
        'article' : bannernews['article'],
        'image' : bannernews['image'],
    } for bannernews in bannernews_list]

    return jp.JSONResponse(result)

def serve_bannernews_image(request):
    filename = request.path_params["name"]
    image_directory = 'images/bannernews/'

    with open(image_directory + filename, 'rb') as f:
        image_data = f.read()
    content_type = 'image/png'
    return jp.HTMLResponse(content=image_data, media_type=content_type)