Basic_things package
=================================================

Пакет общих утилит, использующихся в разных модулях проекта.

Скрипт decorators.py
---------------

.. automodule:: basic_things.decorators
	:members:
	
Скрипт descryptors.py
---------------------

.. autoclass:: basic_things.descryptors.Port
    :members:
   
Скрипт errors.py
---------------------
   
.. autoclass:: basic_things.errors.ServerError
   :members:
   
Скрипт metaclasses.py
-----------------------

.. autoclass:: basic_things.metaclasses.ServerMaker
   :members:
   
.. autoclass:: basic_things.metaclasses.ClientMaker
   :members:
   
Скрипт common_utils.py
---------------------

common.utils. **get_message** (client)


	Функция приёма сообщений от удалённых компьютеров. Принимает сообщения JSON,
	декодирует полученное сообщение и проверяет что получен словарь.

common.utils. **send_message** (sock, message)


	Функция отправки словарей через сокет. Кодирует словарь в формат JSON и отправляет через сокет.


Скрипт main_variables.py
---------------------

Содержит разные глобальные переменные проекта.