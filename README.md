# template-transformer

This tools allow replace plain text(NOT REGULAR EXPRESSION) on a template file(.html, .sh, etc)
It use a dictionary properties file with the format:

property-name = property-value

and the pattern: <<EXPRESSION-TO-REPLACE>>

The pattern is case sensitive.

EXAMPLE:

 ./template_transformer.py properties.txt template.sh result.sh

 NOTE: You don't need to install some extra python library.
 This script run on Amazon Linux.