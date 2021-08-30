# template-transformer

This tools allow replace plain text(NOT REGULAR EXPRESSION) on a template file(.html, .sh, etc)
It use a dictionary properties file with the format:

property-name = property-value

and the pattern: ![image](https://user-images.githubusercontent.com/13359821/131381352-f1af2c76-56dd-4052-b9f7-94841bdd9a10.png)

The pattern is case sensitive.

EXAMPLE:

 ./template_transformer.py properties.txt template.sh result.sh

 NOTE: You don't need to install some extra python library.
 This script run on Amazon Linux.
