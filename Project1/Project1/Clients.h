#pragma once
#include <iostream>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;
class Clients
{
public:
	void Regist();
	void SavingAccount(vector<string>);
	void Sign_in();
};

bool CheckDuplicateUsername(string);
bool CheckAccountList(vector<string>);