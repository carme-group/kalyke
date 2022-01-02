Kalyke
======

TODO:
* Add starship.rs (with reasonable configuration)
* ADd /opt/kalyke/venv/jupyter/bin/ to the PATH

Kalyke is smaller moon of Jupiter,
part of the Carme group.
The
Kalyke
container
is designed to be running locally.

.. code::

    $ docker run -d --name kalyke -p 8888:8888 quay.io/jsconway/kalyke
    $ docker exec -u developer kalyke \
     /opt/kalyke/venv/jupyter/bin/jupyter server list
    Currently running servers:
    http://<HEX>:8888/?token=<TOKEN> :: /opt/kalyke/homedir/src

Copy the token,
and open
:code:`http://127.0.0.1:8888/`
in your browser.
Paste the token into the appropriate field.
