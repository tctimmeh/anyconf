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
  </tbody>
</table>

Supported Python Versions
-------------------------
* 2.6
* 2.7
* 3.2

