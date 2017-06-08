Elegant Concurrency
===================

It's the example codes of “Elegant Concurrency” talk in `PyCon TW 2017
<https://tw.pycon.org/2017/>`_. The slides will release later.

The files are grouped into three parts.


Channel-Based Concurrency
-------------------------

1. `consume_urls_with_task_done.py
   <https://github.com/moskytw/elegant-concurrency-lab/blob/master/consume_urls_with_task_done.py>`_
   – The traditional way we use the queue.
2. `consume_urls_with_channel.py
   <https://github.com/moskytw/elegant-concurrency-lab/blob/master/consume_urls_with_channel.py>`_
   – Apply the channel concept.


Layered Channel-Based Concurrency
---------------------------------

1. `atomic_utils.py
   <https://github.com/moskytw/elegant-concurrency-lab/blob/master/atomic_utils.py>`_
   – The layer of atomic utils.
2. `channel_operators.py
   <https://github.com/moskytw/elegant-concurrency-lab/blob/master/channel_operators.py>`_
   – The layer of channel operators.
3. `graph_initializer.py
   <https://github.com/moskytw/elegant-concurrency-lab/blob/master/graph_initializer.py>`_
   – The layer of graph initializer.


Others
------

Some interesting but minor topics.


Have fun!
