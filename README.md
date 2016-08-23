# pygron

`pygron` helps you easily analyze and grep through JSON.

## Installation
It is advisable to install `pygron` in a virtual environment.

Clone this repo using the following command:
<pre>
$ git clone https://github.com/akshbn/pygron
$ cd pygron
</pre>

Install pygron :

`python setup.py install`

## Usage and examples
pygron converts json into a set of assignment statements. The left hand side of the statement contains the path to the attribute from the root of the json object. The  right hand side is the value of that attribute.

<pre>
$ pygron https://api.github.com/repos/akshbn/pygron/commits | grep "commit.author"
  json[0].commit.author.date = 2016-08-17T11:12:41Z
  json[0].commit.author.email = akshbn@users.noreply.github.com
  json[0].commit.author.name = Akshay B N
  ...
</pre>

Here date is the attribute, which is present within *author* which in turn is present within *commit*.

**Pygron** also supports reading JSON from a file as well as writing output to a file.

To read json from a file:

`$ pygron -f <path to file>`

To write output to a file:

`$ pygron <url> -w`

pygron will write into a file called *pygron_output.txt* in the current working directory.

**Note:** This is a python implementation of [gron](https://github.com/tomnomnom/gron).
