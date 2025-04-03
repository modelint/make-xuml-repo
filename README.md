# Make an Executable UML Repository

Creates a model repository database from a Shlaer-Mellor Executable UML metamodel.

The latest [Shlaer-Mellor metamodel](https://github.com/modelint/shlaer-mellor-metamodel/wiki) is specified inside this package as a folder of .xcm (executable class model) files and a types.yaml file.

Each subsystem of the metamodel (class-attribute, state, etc) is defined in a single .xcm file all within a single foler. That folder also contains one types.yaml file specifying the db type (data type) to use for each metamodel attribute type. The db type 'string', for example, is associated with the `State Name` metamodel type.

We target the little known, but exceptionally useful TclRAL database. It's lean and mean and supports a true relational algebra as defined by [C.J. Date and Hugh Darwen](https://github.com/modelint/shlaer-mellor-metamodel/wiki/Resources#ttm-databases-types-and-the-relational-model-the-third-manifesto-cj-date-hugh-darwen----links-to-the-actual-book-as-a-downloadable-pdf). So we can use nested relational algrebra without any of that SQL mess. It is implemented in C and Tcl, but we provide a python front end called PyRAL to keep everything pythonic.

### Why you need this

You probably don't. What you want instead is the metamodel populator which does use this package.
It's not up on PyPI yet. Give me a couple of weeks and it should be here. I'll post a link when it's ready.

Though if you did want to fiddle with the metamodel, generate your own variation of it and such, this package
might come in handy.

### Installation

Create or use a python 3.11+ environment (early python versions may or may not work).

% pip install make-xuml-repo

At this point you can invoke the repository generator via the command line.

#### From the command line

With the default usage just type:

    % makexumlrepo

Two files will be created in this directory as a result. An mmdb.ral file and a mmclass_ntuples.py file.

The mmdb.ral file is actually a text file that can be opened by TclRAL (via PyRAL) and it will establish an empty relvar per
metamodel class. You can use the previously mentioned populator, or your own, to load it up with
instances of your modeled domains.

The mmclass_ntuples.py file is a handy set of python named tuples. Each named tuple corresponds to a
metamodel class and provides a field for each attribute of that class. PyRal then uses this to insert one or
more tuples into the corresponding relvar.

In my case, I generate the two files and then copy them into my metamodel populator package.