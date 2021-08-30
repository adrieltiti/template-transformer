# template-transformer

This tools allow replace plain text(NOT REGULAR EXPRESSION) on a template file(.html, .sh, etc)
It use a dictionary properties file with the format:

property-name = property-value

and the pattern: ![image](https://user-images.githubusercontent.com/13359821/131395587-af3a137b-f8a8-4ea9-a0f9-085b8cc78fb1.png)


Example:
![image]![image](https://user-images.githubusercontent.com/13359821/131395402-1e3b680d-1802-4a8d-a904-34aaaca95b93.png)



The pattern is case sensitive.

EXAMPLE:

 ./template_transformer.py properties.txt template.sh result.sh

 NOTE: You don't need to install some extra python library.
 This script run on Amazon Linux.
