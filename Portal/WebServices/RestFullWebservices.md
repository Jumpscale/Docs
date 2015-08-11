RestfullWebservices.
====================

It is also possible to use CRUD actions on your defined objects.

To allow this, you need to specify your objects. And then adapt the
generated CRUD functions to your expected behaviour.

The url structure is always like this:

The system app has a simple example to demonstrate this. It contains one
object a *book*.

So the following calls are possible.

List all books

Create a book

The data field of the post contains then the parameters. E.g for a
application/x-www-form-urlencoded content this will name=Lord Of the
Rings&summary=Fantasy Epos

Returs book with id 3

Deletes book 3

It is important to understand that the id always is passed to the
function as id.

E.g in the above example is 3 the value of the id argument.

Using AngularJS.
----------------

See example code in the example dir of the pylabs repository
