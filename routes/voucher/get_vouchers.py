# routes/voucher/get_vouchers.py
import justpy as jp
from models.mongodb.db import db
from models.mongodb.voucher import Voucher

# routes/voucher/get_vouchers.py
def get_vouchers():
    vouchers_list = list(db['vouchers'].find({}))

    result = [{
        'voucher_id': voucher['voucher_id'],
        'image': voucher['image'],
        'priceDiscount': voucher['priceDiscount'],
        'priceDeduct': voucher['priceDeduct'],
        'expiryDate': voucher['expiryDate'],
        'activated': voucher['activated'],
    }   for voucher in vouchers_list]
    return jp.JSONResponse(result)

def serve_voucher_image(request):
    filename = request.path_params["name"]
    image_directory = 'images/vouchers/'

    with open(image_directory + filename, 'rb') as f:
        image_data = f.read()

    content_type = 'image/png'

    return jp.HTMLResponse(content=image_data, media_type=content_type)

# from flask import Flask, Blueprint, jsonify, send_from_directory
# from models.mongodb.db import db
# from models.mongodb.voucher import Voucher
# from blueprints import voucher_bp

# # Displays all objects of User in JSON format on the browser
# @voucher_bp.route('/get_vouchers', methods=['GET'])
# def get_vouchers():
#     vouchers_list = list(db['vouchers'].find({}))

#     result = [{
#         'voucher_id': voucher['voucher_id'],
#         'image': voucher['image'],
#         'priceDiscount': voucher['priceDiscount'],
#         'priceDeduct': voucher['priceDeduct'],
#         'expiryDate': voucher['expiryDate'],
#         'activated': voucher['activated'],
#     }   for voucher in vouchers_list]
#     return jsonify(result)

# @voucher_bp.route('/static/images/voucher/<path:filename>')
# def serve_voucher_image(filename):
#     return send_from_directory('static/images/voucher/', filename)

# # Function to fetch vouchers specifically for create_token_new_user
# def get_vouchers2():
#     vouchers_list = list(db['vouchers'].find({}))
#     result = [{
#         'voucher_id': voucher['voucher_id'],
#         'image': voucher['image'],
#         'priceDiscount': voucher['priceDiscount'],
#         'priceDeduct': voucher['priceDeduct'],
#         'expiryDate': voucher['expiryDate'],
#         'activated': voucher['activated'],
#     } for voucher in vouchers_list]
#     return result