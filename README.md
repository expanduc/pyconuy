PyConUY 2013 contest
====================
This is a PyConUy 2013
[contest](http://www.expand.com.uy/novedades/concurso-pycon-2013/) about
developing a library to interface with [Expand](http://www.expand.com.uy/)
Speaker API.


Why?
===
We use Python in a large portion of our projets and we wanted the PyConUY
attendees to know about it.


Objective
=========
The objective is simple, create a Python library to ease the usage of our
REST-ish speaker voice recognition API documented in
[docs/api.rst](docs/api.rst).
There is also a live demo using this very same API accesible by telephone at
+598 27123142 (instructions are in Spanish).

The version of this public webservice only supports male/female gender
recognition, so the coding task should not be too hard nor long.
To get you started, you can check out the very basic client example
at [example/gender.py](example/gender.py).


Rules
=====
The rules are simple, you spend a bit of time coding, we got to choose the one
we like the most. Only open licensed software is allowed to be used and you can
team up with as many developers as you like.

We watch out for, but not limited to:

* Automated tests.
* How functionally complete the library is.
* The right degree of abstraction.
* Documentation, usage of a framework for this end is a plus.
* PEP8 complaint code.
* Few dependencies.
* Reported API bugs thru this repository Issue system. This includes
  documentation errors.



How to participate
==================
Fork this repo and issue a "pull request" before November 10th. Keep an
eye for updates to this README and API documentation.


Prize
=====
The prize -besides the glory- is a Lenovo IdeaTab A2107 tablet.

We'll make a decision on November 18th and announce the happy winner
right here in this file.

Just git pull the results.


Winner
======
There were two PRs.

[marcelord](https://github.com/marcelor/pyconuy) reported several issues, and
the library was documented using Sphinx, which we love.
The code was functional and quite easy to follow, yet it introduced some
concepts as endpoints which weren't that much natural for us. Also, no audio
file handling was included, which we would like to be included as this is a big
part of the API usage.

Let's talk about [tooxies's](https://github.com/tooxie/pyconuy) work now.
We loved the level of abstraction of his library, it was well balanced, and
included test suites. The code was extremely well documented, but lacked
auto-generated documentation, that we would have appreciated. However, good
documentation and usage examples where supplied, so it was easy to follow the
code and understand how the library worked.

No submission was 100% PEP8 compliant but tooxie's was by far the most rigorous
in that matter. This submission also had automatic audio file handling,
including automatic conversion, which is fantastic feature to have.
tooxie also reported a couple of issues via github.

We found tooxie's version the most pythonic and functionally complete, and
that's why we choose it as the winner.

Congratulations to both and thank you very much for your submissions.

