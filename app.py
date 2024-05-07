# app.py
import justpy as jp
from config import IPV4_ADDRESS
from models.mongodb.create_collections import create_collections
# Route imports
from routes.frontpage.frontpage import frontpage
from routes.fullnews.get_fullnews import get_fullnews
from routes.fullnews.get_fullnews import serve_fullnews_image
from routes.bannernews.get_bannernews import get_bannernews
from routes.bannernews.get_bannernews import serve_bannernews_image
from routes.menuitem.get_menuitem import get_menuitem
from routes.menuitem.get_menuitem import serve_menuitem_image

# Route declarations
jp.Route('/', frontpage)
jp.Route('/get_fullnews', get_fullnews)
jp.Route('/static/images/fullnews/{name}', serve_fullnews_image)
jp.Route('/get_bannernews', get_bannernews)
jp.Route('/static/images/bannernews/{name}', serve_bannernews_image)
jp.Route('/get_menuitem', get_menuitem)
jp.Route('/static/images/menuitem/{name}', serve_menuitem_image)

# Create starting dataset collections for the app. 
create_collections()

# Start the app on the address
# debug= True is to allow hot reload during coding, but set to false or remove when deploying for real.
jp.justpy(host=IPV4_ADDRESS, debug=True)

