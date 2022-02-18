============
simple_https
============


.. image:: https://img.shields.io/pypi/v/simple_https.svg
        :target: https://pypi.python.org/pypi/simple_https

.. image:: https://img.shields.io/travis/wwj718/simple_https.svg
        :target: https://travis-ci.org/wwj718/simple_https

.. image:: https://readthedocs.org/projects/simple-https/badge/?version=latest
        :target: https://simple-https.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




simple https server. 

Just like 'python3 -m http.server', but https.


* Free software: GNU General Public License v3
* Documentation: https://simple-https.readthedocs.io.


Install
-------

pip install simple_https

Usage
-----

work with mkcert: https://github.com/FiloSottile/mkcert



mkcert -install

mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1

simple-https -k ~/example.com+5-key.pem -c ~/example.com+5.pem



Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
