# Project description

This is a simple bibliography application for viewing and creating collections of records for documents. It was made as a portfolio project and for learning purposes only.

It has the following functionality:

* Defining statements of responsibility (author, publisher etc.)
* Adding to the database:
    * Bibliographic descriptions of documents
    * Personal records for authors, illustrators, translators etc.
    * Records for collective bodies such as publishing houses, foundations etc.;
    * geographic locations, languages, document types, statements of responsibility
* Defining document topics (subject keywords, geographic locations, individuals etc.)
* Browsing, searching and editing collected information
* Registering and authenticating bibliography editors and managing their accounts.

I chose to write a simplified bibliography web application for the following reasons:

* It gave me the opportunity to practice using relational database with various relationships between tables.
* Bibliographies are something I used to learn about while I was studying at the university.

## What is the difference between bibliography and library management system?

Bibliographies and bibliography applications are similar to library management systems in that they register documents (bibliographic entries).

The main difference is that the bibliography records characteristics of all copies of a given book as a single publication, whereas library management system also records particular physical copies of a document (among other functionality).

The aim of a bibliography is to inform users about documents published and allow them to browse bibliographic descriptions using different criteria (such as topics of a document; it's author, publication place etc.)

I took Polska Bibliografia Literacka (Polish Bibliography of Literature available at http://www.ibl.poznan.pl/) as a very general model for my application (mainly in respect to it's purpose).

## Technologies used

This is my first attempt to create a web application. It serves the purpose of learning and, at the same time, practicing the following tools, frameworks, technologies and skills:

* Flask web framework
* Jinja2 templating mechanism
* SQLAlchemy Object-Relational Mapper (ORM)
* Python programming language
* HTML + Bootstrap
* Designing database using Entity-Relationship (ER) diagrams
* Using MySQL Workbench as a database design tool
* PyUnit testing framework
* UML use-case diagrams
* Elasticsearch (for searching the database)
* Writing software requirements document (which is available [here](https://docs.google.com/document/d/1l2sDb6wOPnfhyzBBr6hmPlrVnx5hCmTDyNj_LDbgHxs/edit?usp=sharing))
* JavaScript (with JQuery - basics of which I learnt during writing the code, just as I did with Bootstrap)
* Object-oriented paradigm as well as taking advantage of functions as first-class citizens in both Python and JS
* Basics of Git
* SQLite database

I used Emacs for writing most of the code, including Jinja2 templates (Emacs has also a mode for Jinja2 syntax). Occasionally, I was using ActiveState Komodo text editor for better html and JS code formatting.

## References:
During (and before) the development of the application I familiarized myself with the following resources (books, learning materials, official documentation and websites):

### Books:
* Duckett, Jon. *HTML & CSS. Design and Build Websites.* Indianapolis, 2011.
* Grinberg, Miguel. *Flask Web Development: Developing Web Applications with Python.* \[Sebastopol\], 2018.
* Haverbeke, Marijn. Eloquent JavaScript. 3rd edition. 2018 (available online: https://eloquentjavascript.net/)
* Lutz, Mark. Learning Python. [Sebastopol], 2009.
* Pratt, Phil; Last, Mary. *Concepts of Database Management.* Boston, 2014. (Fragments only)
* Sommerville, Ian. *Software Engineering.* Boston, 2016.

### Websites (last accessed on December 30, 2021):
* Bootstrap 4 documentation - https://getbootstrap.com/
* JQuery documentation - https://jquery.com/
* MDN Web Docs (Mozilla developer's docs - include reference on JavaScript and HTML, among other Web technologies) - https://developer.mozilla.org/en-US/
* Real Python (Emacs configuration for use with Python, useful posts about Python and it's features) - https://realpython.com/
* Miguel Grinberg's blog about Python, Flask and much more: https://blog.miguelgrinberg.com/
* SQLAlchemy documentation - https://docs.sqlalchemy.org/en/14/
* StackOverflow (usually browsing already answered questions): https://stackoverflow.com/

[Working installation screen-record - description of steps performed is currently in Polish](https://youtu.be/QaYa7rLCeNw)


Copyright© 2022 Radosław Kuzyk
## Disclaimer

This software is provided by the copyright holder “as is” and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. In no event shall the copyright owner be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.
Based on/source: [The 3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause)
