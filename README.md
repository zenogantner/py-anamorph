py-anamorph
===========

morphological analysis command-line tools in Python (currently limited to German)


Limitations
-----------

`analyze-substantives.py` currently only supports substantive (noun) analysis for the nominal case.

The functionality should be very easy to enhance.
Send a pull-request if you have something to contribute!

The tool is not optimized for latency or throughput, do not use it for large-scale work:
It uses a brute-force approach with a full form lexicon stored in a hashmap.


Examples
--------

    echo "Bier Woche Restaurants" | ./analyze-substantives.py morphy-export-substantives-NOM.tsv.gz 
    Bier
      Bier NOM SIN NEU
    Woche
      Woche NOM SIN FEM
    Restaurants
      Restaurant NOM PLU NEU


    echo "Bier Woche Restaurants" | ./analyze-substantives.py morphy-export-substantives.tsv.gz
    Bier
      Bier NOM SIN NEU
      Bier DAT SIN NEU
      Bier AKK SIN NEU
    Woche
      Woche NOM SIN FEM
      Woche GEN SIN FEM
      Woche DAT SIN FEM
      Woche AKK SIN FEM
    Restaurants
      Restaurant GEN SIN NEU
      Restaurant NOM PLU NEU
      Restaurant GEN PLU NEU
      Restaurant DAT PLU NEU
      Restaurant AKK PLU NEU


Copyright & Licensing
---------------------

Copyright (C) 2014 Zeno Gantner

py-anamorph is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-anamorph is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with py-anamorph.  If not, see <http://www.gnu.org/licenses/>.

----

The data files `morphy-export-substantives-NOM.tsv.gz` and `morphy-export-substantives.tsv.gz`
are derived from the
[Morphy export file](http://www.danielnaber.de/morphologie/morphy-export-20110722.tar.gz)
by Daniel Naber,
which is licensed under [CC-BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).
See [http://www.danielnaber.de/morphologie/](http://www.danielnaber.de/morphologie/) for more information.



