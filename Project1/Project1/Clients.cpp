#include "Clients.h"

void Clients:: Regist()
{
	vector<string>account;
	string username, password;
	cout << "Registion." << endl;
	cout << "Enter your username: ";
	cin >> username;
	while (CheckDuplicateUsername(username))
	{
		cout << "This username is already exist, please choose another one." << endl;
		cout << "Enter your username: ";
		cin >> username;
	}
	account.push_back(username);
	cout << endl;

	cout << "Enter your password: ";
	cin >> password;
	account.push_back(password);

	SavingAccount(account);
}

void Clients::SavingAccount(vector<string>account)
{
	ofstream writer("AccountsList.txt", ios::app);
	writer << account[0] << ";" << account[1]<<endl;
	writer.close();
}

bool CheckDuplicateUsername(string username)
{
	
	vector<string> usernamesList;
	ifstream reader("AccountsList.txt", ios::in);
	string temp;
	int n=-1;// vì dòng cuối rỗng ( blank line)
	
	while (!reader.eof())
	{
		getline(reader, temp);
		n++;
	}
	reader.clear();
	reader.seekg(0);

	for (int i = 0; i < n; ++i)
	{
		getline(reader, temp, ';');
		usernamesList.push_back(temp);
		getline(reader, temp);
	}

	for (int i = 0; i < usernamesList.size(); ++i)
	{
		if (username == usernamesList[i])
			return 1;
	}

	reader.close();
	return 0;
}

void Clients::Sign_in()
{
	vector<string>account;
	cout << "Sign in." << endl;
	string username, password;
	cout << "Enter your username: ";
	cin >> username;
	account.push_back(username);
	cout << endl;

	cout << "Enter your password: ";
	cin >> password;
	account.push_back(password);
	while (CheckAccountList(account)==0)
	{
		account.clear();
		cout << "This account is not exist, please enter again." << endl;
		cout << "Enter your username: ";
		cin >> username;
		account.push_back(username);
		cout << endl;

		cout << "Enter your password: ";
		cin >> password;
		account.push_back(password);
	}
	cout << "Sign in success,welcome to the Online Librabry.";
}

 bool CheckAccountList(vector<string>account)
{
	vector<string> usernamesList;
	vector<string> passwordsList;
	ifstream reader("AccountsList.txt", ios::in);
	string temp;
	int n = -1;// vì dòng cuối rỗng ( blank line)

	while (!reader.eof())
	{
		getline(reader, temp);
		n++;
	}
	reader.clear();
	reader.seekg(0);

	for (int i = 0; i < n; ++i)
	{
		getline(reader, temp, ';');
		usernamesList.push_back(temp);
		getline(reader, temp);
		passwordsList.push_back(temp);
	}

	for (int i = 0; i < usernamesList.size(); ++i)
	{
		if (account[0] == usernamesList[i])
		{
			if (account[1] == passwordsList[i])
				return 1;
		}
	}
	return 0;

	reader.close();
}

