hepsi: program
program:
	g++ -I "./include" -c ./src/Yigin.cpp -o  ./lib/Yigin.o
	g++ -I "./include" -c ./src/YiginDizisi.cpp -o  ./lib/YiginDizisi.o
	g++ -I "./include" -c ./src/Yonetim.cpp -o  ./lib/Yonetim.o
	g++ -I "./include" -c ./src/main.cpp  -o ./lib/main.o
	g++ ./lib/Yigin.o ./lib/YiginDizisi.o ./lib/main.o ./lib/Yonetim.o -o ./bin/program
	./bin/program