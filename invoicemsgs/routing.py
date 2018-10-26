from channels.routing import route
from invoicemsgs.consumers import ws_connect, ws_disconnect, ws_message


channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
    route("websocket.receive", ws_message),
]
# from channels.routing import ProtocolTypeRouter

# application = ProtocolTypeRouter({
#     # Empty for now (http->django views is added by default)
# })
