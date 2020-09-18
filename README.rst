sche
========


.. image:: https://api.travis-ci.org/dbader/schedule.svg?branch=master
        :target: https://travis-ci.org/dbader/schedule

.. image:: https://coveralls.io/repos/dbader/schedule/badge.svg?branch=master
        :target: https://coveralls.io/r/dbader/schedule

.. image:: https://img.shields.io/pypi/v/schedule.svg
        :target: https://pypi.python.org/pypi/schedule

`sche` is a fork of `schedule` -- Python job scheduling for humans.

An in-process scheduler for periodic jobs that uses the builder pattern
for configuration. Schedule lets you run Python functions (or any other
callable) periodically at pre-determined intervals using a simple,
human-friendly syntax.

Inspired by `Adam Wiggins' <https://github.com/adamwiggins>`_ article `"Rethinking Cron" <https://adam.herokuapp.com/past/2010/4/13/rethinking_cron/>`_ and the `clockwork <https://github.com/Rykian/clockwork>`_ Ruby module.

Features
--------
- A simple to use API for scheduling jobs.
- Very lightweight and no external dependencies.
- Excellent test coverage.
- Tested on Python 3.6+
- Timezone support.

Usage
-----

.. code-block:: bash

    $ pip install sche

.. code-block:: python

    import sche
    import time

    def job():
        print("I'm working...")

    sche.every(10).minutes.do(job)
    sche.every().hour.do(job)
    sche.every().day.at("10:30").do(job)
    sche.every(5).to(10).minutes.do(job)
    sche.every().monday.do(job)
    sche.every().wednesday.at("13:15").do(job)
    sche.every().minute.at(":17").do(job)

    # or use schedule expression
    sche.when("every 10 minutes").do(job)
    sche.when("every hour").do(job)
    sche.when("every day at 10:30").do(job)
    sche.when("every 5 to 10 minutes").do(job)
    sche.when("every monday").do(job)
    sche.when("every wednesday at 13:15").do(job)
    sche.when("every minute at :17").do(job)

    # or use decorator to register job(without arguments)
    @sche.when("every 10 minutes")
    def another_job():
        print("I'm working on another job...")

    sche.clear()  # remove all jobs

    # set job with timezone
    sche.timezone("+0800").every().day.at("00:00").do(job)

    sche.run_forever()

Documentation
-------------

`sche`'s documentation lives at `sche.readthedocs.io <https://sche.readthedocs.io/>`_.

Please also check the FAQ there with common questions.


Meta
----

Daniel Bader - `@dbader_org <https://twitter.com/dbader_org>`_ - mail@dbader.org

Distributed under the MIT license. See `LICENSE.txt <https://github.com/dbader/schedule/blob/master/LICENSE.txt>`_ for more information.

https://github.com/dbader/schedule
