# fabric-generator

## TODO
    bél client link, taamel dossier ekher, as2él wessim
## USAGE
    python3 main.py fabric_name fabric_location jpg 123456-12345 seamless inches keep_ratio color path1 path2 path3 size cut type client
    python3 main.py fabric_name fabric_location jpg 123456-12345 0 2 0 FFFFFF path1 path2 path3 42 quarter 36evenweave StitcheryXpress.com
    python3 main.py fabric_name fabric_location jpg 123456-12345 1 2 0 FFFFFF path1 path2 path3 42 quarter 36evenweave
    python3 main.py fabric_name fabric_location jpg 123456-12345 0 2 0 FFFFFF path1 path2 path3 all StitcheryXpress.com
    python3 main.py fabric_name fabric_location jpg 123456-12345 1 2 0 FFFFFF path1 path2 path3 all

    - Generate all
    >py main.py test fabric jpg 123456-12345 0 2 0 FFFFFF C:\Users\Bouzazi\Documents\Gev\fabric-generator\ C:\Users\Bouzazi\Documents\Gev\fabric-generator\generated\ C:\Users\Bouzazi\Documents\Gev\fabric-generator\masterfiles\ all

    - Geneate a specific image
    >py main.py test fabric jpg 123456-12345 0 2 0 FFFFFF C:\Users\Bouzazi\Documents\Gev\fabric-generator\ C:\Users\Bouzazi\Documents\Gev\fabric-generator\generated\ C:\Users\Bouzazi\Documents\Gev\fabric-generator\masterfiles\ 42 quarter 36evenweave StitcheryXpress.com