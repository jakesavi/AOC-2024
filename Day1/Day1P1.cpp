#include <algorithm>
#include <bits/stdc++.h>
#include <cstddef>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <ostream>
#include <string>
#include <vector>

std::vector<std::string> SplitLines(std::string line) {
  std::string Delimiter = " ";
  // Result Stores a split between both strings. So like: (27484, 55634)
  std::vector<std::string> results;
	std::string token;
	size_t pos = 0;
	std::string delimiter = "   ";
	while((pos = line.find(delimiter)) != std::string::npos){
		token = line.substr(0,pos);
		results.push_back(token);
		line.erase(0,pos+delimiter.length());
	}
	results.push_back(line);
	return results;
}



std::vector<int> ReturnDistanceVector(std::string FileName) {
  std::vector<int> LeftList; // LeftList Must Not Change.
  std::vector<int> RightList;

  std::ifstream file("FileName.txt");
  if (!file.is_open()) {
    std::cerr << "Error Opening File";
  }
	std::string line;
	while (std::getline(file, line)) {
		std::vector<std::string> LineSplit = SplitLines(line);
	}
  file.close();
}

int main() {
  // Given a list of 2 elements, We must find the distance between both.
  // Start Smallest then go up from there. We could also find matches AS IS.
  // This may improve run time making it O(n) instead of O(n^2)
	for (const std::string &s : SplitLines("28484   55634")){
		std::cout << s << std::endl;
			
	}
}
