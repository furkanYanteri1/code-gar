hepsi: program
program:
	g++ -I "./include" -c ./src/Sinif.cpp -o  ./lib/Sinif.o
	g++ -I "./include" -c ./src/Ogrenci.cpp -o  ./lib/Ogrenci.o
	g++ -I "./include" -c ./src/Okul.cpp -o  ./lib/Okul.o
	g++ -I "./include" -c ./src/main.cpp  -o ./lib/main.o
	g++ ./lib/Sinif.o ./lib/Okul.o ./lib/main.o ./lib/Ogrenci.o -o ./bin/program
	./bin/program