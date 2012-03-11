AnyConf
=======

AnyConf is a configuration library for python that wraps several other configuration libraries under a common API. Some
uses of AnyConf include:

* Support more than one file format for configuration data
* Maintain agility to switch formats later
* Defer a decision about which format(s) to support

Limitations
-----------
AnyConf makes use of existing configuration libraries. It does not re-implement the functionality itself. Obviously, not
all libraries have the same set of capabilities. While AnyConf tries to be as flexible as possible there will naturally
be some features that cannot be supported under a generic API.

The behaviours and capabilities of the libraries that AnyConf depends on may change between releases. Applications
written for specific versions of python or configuration libraries should be aware of how these changes may affect their
configuration data. AnyConf makes no attempt to compensate for these behavioural changes.

Usage
-----
Create a new ConfigLoader and load your configuration data from a file-like object.

    import anyconf
    config = anyconf.ConfigLoader()
    config.load(myOpenFile, anyconf.FORMAT_INI)

The exact methods that the file-like object needs to support are dependant on what the underlying configuration library
requires. For instance, `.ini` files use the `configparser` module, which only requires the `readline` method.

The returned `Config` object can be traversed in a hierarchical manner, referencing child sections and options as
properties or dict items. Use the dict notation when a configuration item might conflict with a python keyword or
library method, or contain characters that are illegal in property names (such as spaces).

    configValue config.someSection.someOption
    anotherValue = config["another section"]["another option"]

Supported Formats
-----------------

<table>
  <thead>
    <tr>
      <td>Format</td>
      <td>Underlying Library</td>
      <td>Notes</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>.ini</td>
      <td><a href="http://docs.python.org/dev/library/configparser.html">configparser</a></td>
      <td>Uses <a href="http://docs.python.org/library/configparser.html">ConfigParser</a> in python 2</td>
    </tr>
    <tr>
      <td>.xml</td>
      <td><a href="http://docs.python.org/release/3.1.3/library/xml.dom.minidom.html">minidom</a></td>
      <td></td>
    </tr>
  </tbody>
</table>

Supported Python Versions
-------------------------
* 2.5
* 2.6
* 2.7
* 3.1
* 3.2

Format Mappings
---------------

This section demonstrates how AnyConf maps each file format to python objects.

### XML ###

<table>
  <thead>
    <tr>
      <td>XML Source</td>
      <td>Python Representation</td>
      <td>Comments</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&lt;e&gt;<br />&nbsp;&nbsp;my text<br />&nbsp;&nbsp;goes here<br />&lt;/e&gt;</td>
      <td>config.e == 'my text\n  goes here'</td>
      <td>Accessing an element that contains only CDATA text returns that text as the value of the option with leading
          and trailing whitespace removed.</td>
    </tr>
    <tr>
      <td>&lt;e&gt;<br />
          &nbsp;&nbsp;&lt;a&gt;true&lt;/a&gt;<br />
          &nbsp;&nbsp;&lt;b&gt;false&lt;/b&gt;<br />
          &nbsp;&nbsp;&lt;c&nbsp;/&gt;<br />
          &lt;/e&gt;</td>
      <td>config.e.a == True<br />
          config.e.b == False<br />
          config.e.c == True</td>
      <td>Case-insensitive "true" and "false" become the boolean True and False respectively. Blank text also become
          the boolean True.</td>
    </tr>
    <tr>
      <td>&lt;e option=&quot;value&quot; /&gt;</td>
      <td>config.e.option == 'value'</td>
      <td>Element attributes can also be read as configuration options.</td>
    </tr>
    <tr>
      <td>&lt;e&gt;<br />
          &nbsp;&nbsp;&lt;f&gt;something&lt;/f&gt;<br />
          &lt;/e&gt;</td>
      <td>config.e.f == 'something'</td>
      <td>Nested elements form a hierarchy of python objects.</td>
    </tr>
    <tr>
      <td>&lt;e&gt;<br />
          &nbsp;&nbsp;&lt;f attr=&quot;first&quot; /&gt;<br />
          &nbsp;&nbsp;&lt;f attr=&quot;second&quot; /&gt;<br />
          &lt;/e&gt;</td>
      <td>config.e.f[0].attr == 'first'<br />
          config.e.f[1].attr == 'second'<br /></td>
      <td>If an element has more than one child with the same name then they are represented as a list of options.</td>
    </tr>
  </tbody>
</table>

#### Notes ####

* Elements with attributes or child elements *ignore* their CDATA text. It is best to encapsulate all text within an
  element and avoid attributes altogether.
* Use the `getAsList` method for options that may be lists of less than 2 elements to guarantee that the API will
  always return a list.
