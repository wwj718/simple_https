# -*- coding: utf-8 -*-
"""Main module."""
import argparse
import os
import http.server, ssl

base_path = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.join(base_path, "src")
server_pem = os.path.join(src_path, "server.pem")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", dest="certfile", default="None", help="certfile")
    parser.add_argument("-p", dest="port", default=8443, help="http server port")
    parser.add_argument("-a", dest="address", default="0.0.0.0", help="address")
    parser.add_argument("-d", dest="directory", default=".", help="directory")
    args = parser.parse_args()

    if args.certfile != 'None':
        certfile = args.certfile
    else:
        certfile = str(server_pem)
        # print("certfile: ", certfile)
        # from IPython import embed;embed()

    server_address = (args.address, args.port)
    httpd = http.server.HTTPServer(server_address,
                                   http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile=certfile, # path
        ssl_version=ssl.PROTOCOL_TLSv1)
    httpd.serve_forever()