# routes/menuitem/get_menuitem.py
import justpy as jp
from models.mongodb.db import db
from models.mongodb.menuitem import MenuItem

def get_menuitem():
    menuitems_list = list(db['menuitem'].find({}))

    result = [{
        'id': item['id'],
        'title': item['title'],
        'description': item['description'],
        'category': item['category'],
        'price': item['price'],
        'imagepath': item['imagepath'],
        'available': item['available'],
        'additions': item['additions'],
        'ingredients': item['ingredients'],
        'userreviews': item['userreviews']
    } for item in menuitems_list]
    return jp.JSONResponse(result)

def serve_menuitem_image(request):
    print("TODO")
    filename = request.path_params["name"]
    image_directory = 'static/images/menuitem/'

    with open(image_directory + filename, 'rb') as f:
        image_data = f.read()

    content_type = 'image/png'

    return jp.HTMLResponse(content=image_data, media_type=content_type)



# routes/menuitem/get_menuitems.py

# from flask import Flask, Blueprint, jsonify, send_from_directory
# from models.mongodb.db import db
# from models.mongodb.menuitem import MenuItem
# from blueprints import menuitem_bp

# Displays all objects of MenuItem in JSON format on the browser
# @menuitem_bp.route('/get_menuitems', methods=['GET'])
# def get_menuitems():
#     menuitems_list = list(db['menuitem'].find({}))

#     result = [{
#         'id': item['id'],
#         'title': item['title'],
#         'description': item['description'],
#         'category': item['category'],
#         'price': item['price'],
#         'imagepath': item['imagepath'],
#         'available': item['available'],
#         'additions': item['additions'],
#         'ingredients': item['ingredients'],
#         'userreviews': item['userreviews']
#     } for item in menuitems_list]

#     return jsonify(result)

# @menuitem_bp.route('/static/images/menuitem/<path:filename>')
# def serve_menuitem_image(filename):
#     return send_from_directory('static/images/menuitem/', filename)