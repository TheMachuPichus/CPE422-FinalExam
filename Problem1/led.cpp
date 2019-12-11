#include <iostream>         // for the input/output
#include <stdlib.h>         // for the getenv call
#include <sys/sysinfo.h>    // for the system uptime call
#include <cgicc/Cgicc.h>    // the cgicc headers
#include <cgicc/CgiDefs.h>
#include <cgicc/HTTPHTMLHeader.h>
#include <cgicc/HTMLClasses.h>
#include <unistd.h>
#define LED_GPIO "/sys/class/gpio/gpio60/"
using namespace std;
using namespace cgicc;

void writeGPIO(string filename, string value){
   fstream fs;
   string path(LED_GPIO);
   fs.open((path + filename).c_str(), fstream::out);
   fs << value;
   fs.close();
}

int  getGPIO(){
     string temp;
     fstream fs;
     fs.open("/sys/class/gpio/gpio60/value",fstream::in);
     fs >> temp;
     fs.close();
     if (temp == "0")
        return 0;
     else if (temp == "1")
        return 1;
     else
        return 2;
  }


int main(){
   int val;
   writeGPIO("direction", "in");
   val = getGPIO();
   // generate the form but use states that are set in the submitted form
   cout << HTTPHTMLHeader() << endl;       // Generate the HTML form
   cout << html() << head() << title("Read Digital") << head() << endl;
   cout << body() << h1("CPE 422/522 Final Exam: Reading Digital Input") << body() << endl;
   cout << body() << h1("Reading a GPIO Pin via a Web Browser") << body() << endl;
   cout << "<form action=\"/cgi-bin/switch.cgi\" method=\"POST\">\n";
   cout << "<input type=\"submit\" value=\"Read Switch\" />";
   cout << body() << h1("Switch State:") << body() << endl;
   cout << "</div></form>";
   
   if (val==0) cout << body() << h1("Off") << body() << endl;              // turn on
   else if (val==1) cout << body() << h1("On") << body() << endl;        // turn off
   else cout << body() << h1("Not Valid input") << body() << endl;
   
   cout << body() << html();
   return 0;
}
