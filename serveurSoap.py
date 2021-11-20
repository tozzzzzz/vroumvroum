# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:05:47 2021

@author: user
"""



import logging
#logging.basicConfig(level=logging.DEBUG)

from spyne import Application, rpc, ServiceBase, Integer, Unicode, AnyDict, Double
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.protocol.xml import XmlDocument
from spyne.server.wsgi import WsgiApplication





from math import acos, asin, atan, atan2, ceil, cos, cosh, degrees
from math import exp, fabs, floor, fmod, frexp, hypot, ldexp, log
from math import log10, modf, pi, pow, radians, sin, sinh, sqrt
from math import tan, tanh


class CalculeDistance(ServiceBase):
	@rpc(Unicode, Unicode, Unicode, Unicode, _returns=Double)
	def get_distance(ctx, lat_1, lng_1, lat_2, lng_2): 
		   lng_1, lat_1, lng_2, lat_2 = map(radians, [float(lng_1), float(lat_1), float(lng_2), float(lat_2)])
		   d_lat = lat_2 - lat_1
		   d_lng = lng_2 - lng_1 

		   temp = (  
			      sin(d_lat / 2) ** 2 
				  + cos(lat_1) 
				  * cos(lat_2) 
				  * sin(d_lng / 2) ** 2
		   )
		   a=6373 * (2 * atan2(sqrt(temp), sqrt(1 - temp)))

           
		   return a
	   
	        


			
application = Application([CalculeDistance],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)



if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()