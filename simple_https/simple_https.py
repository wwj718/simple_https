# -*- coding: utf-8 -*-
"""Main module."""
import argparse
import os
import http.server, ssl

base_path = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.join(base_path, "src")
# server_pem = os.path.join(src_path, "server.pem")

def main():
    '''
    work with mkcert: https://github.com/FiloSottile/mkcert
        mkcert -install
        mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1
    simple-https -k ~/example.com+5-key.pem -c ~/example.com+5.pem
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", dest="certfile", default="None", help="certfile")
    parser.add_argument("-k", dest="keyfile", default="None", help="keyfile")
    parser.add_argument("-p", dest="port", default=8443, help="http server port")
    parser.add_argument("-a", dest="address", default="0.0.0.0", help="address")
    parser.add_argument("-d", dest="directory", default=".", help="directory")
    args = parser.parse_args()

    print(f"Serving HTTPS on {args.address} port {args.port} (https://{args.address}:{args.port}/) ...")
    server_address = (args.address, int(args.port))
    httpd = http.server.HTTPServer(server_address,
                                   http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        keyfile=args.keyfile,
        certfile=args.certfile,  # path
        server_side=True)

    httpd.serve_forever()