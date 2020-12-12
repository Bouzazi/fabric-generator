# fabric-generator
## USAGE
    python3 main.py fabric_name fabric_location jpg 123456-12345 seamless inches keep_ratio landscape/portrait color path1 path2 path3 size cut type client
    python3 main.py fabric_name fabric_location jpg 123456-12345 0 2 0 0 FFFFFF path1 path2 path3 42 quarter 36evenweave StitcheryXpress.com
    python3 main.py fabric_name fabric_location jpg 123456-12345 1 2 0 0 FFFFFF path1 path2 path3 42 quarter 36evenweave
    python3 main.py fabric_name fabric_location jpg 123456-12345 0 2 0 0 FFFFFF path1 path2 path3 all StitcheryXpress.com
    python3 main.py fabric_name fabric_location jpg 123456-12345 1 2 0 0 FFFFFF path1 path2 path3 all

    - Generate all
    >py main.py test cmyk jpg 123456-12345 0 2 0 0 FFFFFF C:\Users\Bouzazi\Documents\Gev\fabric-generator\ C:\Users\Bouzazi\Documents\Gev\fabric-generator\generated\ C:\Users\Bouzazi\Documents\Gev\fabric-generator\masterfiles\ all

    - Geneate a specific image (Windows Example)
    >py main.py test cmyk jpg 123456-12345 0 2 0 0 FFFFFF C:\Users\Bouzazi\Documents\Gev\fabric-generator\ C:\Users\Bouzazi\Documents\Gev\fabric-generator\generated\ C:\Users\Bouzazi\Documents\Gev\fabric-generator\masterfiles\ 42 quarter 36evenweave StitcheryXpress.com

    - Geneate a specific image (Linux Example)
    >python3 main.py test cmyk jpg 123456-12345 0 2 0 0 FFFFFF /Users/mentornations/Documents/fabric-generator-master/ /Users/mentornations/Documents/fabric-generator-master/generated/ /Users/mentornations/Documents/fabric-generator-master/masterfiles/ 42 quarter 36evenweave