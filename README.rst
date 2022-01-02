Kalyke
======

TODO:
* Add starship.rs (with reasonable configuration)
* Add /opt/kalyke/venv/jupyter/bin/ to the PATH
* Put virtualenvwrapper in /opt/kalyke/venv/jupyter/bin/
* Make /opt/kalyke/homedir/.ssh with ownership developer and permissions 700

Kalyke is smaller moon of Jupiter,
part of the Carme group.
The
Kalyke
container
is designed to be running locally.

Running the container
---------------------

The container is designed to be run as a
persistent
one.

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

Using the container
-------------------

Even though the container is designed to be persistent,
every container,
indeed every computer,
eventually needs to return to the void.
The best way to prepare for this eventuality
is to keep code in source control repositories
which are pushed to a centralized place.

After connecting to Jupyter,
open a terminal and run
:code:`ssh-keygen`,
and then run

.. code::

    $ cat ~/.ssh/id_rsa.pub
    ...

Copy the output,
and paste it into your favorite source control server's
SSH key configuration.
Now you can start cloning repositories:

.. code::

    $ git clone git@example.com:myname/repository.git

In order to avoid having to recreate local configuration,
use a
:code:`dotfiles`
code repository
with the relevant configuration.

Some examples are
`Julian's dotfiles`_
or
`moshez's dotfiles`_.


.. _Julian's dotfiles: https://github.com/Julian/dotfiles
.. _moshez's dotfiles: https://github.com/moshez/dotfiles
