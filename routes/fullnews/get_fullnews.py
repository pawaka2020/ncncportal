# routes/fullnews/get_fullnews.py
import justpy as jp
from models.mongodb.db import db
from models.mongodb.fullnews import FullNews

def get_fullnews():
    fullnews_list = list(db['fullnews'].find({}))

    result = [{
        'name' : fullnews['name'],
        } for fullnews in fullnews_list]

    return jp.JSONResponse(result)

def serve_fullnews_image(request):
    filename = request.path_params["name"]
    image_directory = 'images/fullnews/'

    with open(image_directory + filename, 'rb') as f:
        image_data = f.read()

    content_type = 'image/png'

    return jp.HTMLResponse(content=image_data, media_type=content_type)